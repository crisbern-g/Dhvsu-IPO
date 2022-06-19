from django.core.paginator import Paginator
from django.contrib import messages
from django.views import View
from django.shortcuts import redirect, render, get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import UtilityModelApplicationModel
from .forms import AddUtilityModelForm, EditRemarksForm, DraftFileForm, InventionPicturesFileForm, AbstractFileForm, AuthorIdsFileForm, MemorandumOfAppointmentFileForm

# Create your views here.
class UtilityModelHome(LoginRequiredMixin, View):
    login_url = 'login'

    def get(self, request):
        utility_model_applications = UtilityModelApplicationModel.objects.all()

        table_page = Paginator(utility_model_applications, 20)
        current_page = request.GET.get('page')
        utility_models = table_page.get_page(current_page)

        context = {
            'utility_models' : utility_models
        }

        return render(request, 'Utility_Model/home.html', context)


class SearchView(LoginRequiredMixin,View):
    login_url = 'login'

    def get(self, request):
        search_query = request.GET.get('search_query')

        utility_models = UtilityModelApplicationModel.objects.filter(utility_model_application_name__contains=search_query)

        context = {
            'utility_models' : utility_models,
            'query' : search_query
        }

        return render(request, 'Utility_Model/search_results.html', context)


class AddUtilityModelView(LoginRequiredMixin, View):
    login_url = 'login'

    def get(self, request):
        form = AddUtilityModelForm()

        context = {
            'form' : form
        }

        return render(request, 'Utility_Model/add.html', context)


    def post(self, request):
        form = AddUtilityModelForm(request.POST)

        if form.is_valid():
            new_utility_model = form.save(commit=False)
            new_utility_model.save()

            return redirect('utility-model-detail', slug=new_utility_model.utility_model_slug)

        context = {
            'form' : form
        }

        return render(request, 'Utility_Model/add.html', context)


class UtilityModelDetailView(LoginRequiredMixin, View):
    login_url= 'login'

    def get(self, request, slug):
        utility_model_application = get_object_or_404(UtilityModelApplicationModel, utility_model_slug=slug)

        draft_file = utility_model_application.draft_file.first()
        invention_pictures = utility_model_application.invention_pictures.first()
        abstract_file = utility_model_application.abstract_file.first()
        author_ids = utility_model_application.author_ids.first()
        memorandum_of_appointment = utility_model_application.memorandum_of_appointment.first()

        documents = {
            'draft_file' : draft_file,
            'invention_pictures' : invention_pictures,
            'abstract_file' : abstract_file,
            'author_ids' : author_ids,
            'memorandum_of_appointment' :  memorandum_of_appointment,
        }

        context = {
            'documents' : documents,
            'application' : utility_model_application
        }

        return render(request, 'Utility_Model/detail.html', context)


class EditRemarks(LoginRequiredMixin, View):
    login_url = 'login'

    def get(self, request, slug):
        utility_model_application = get_object_or_404(UtilityModelApplicationModel, utility_model_slug=slug)

        form = EditRemarksForm(instance=utility_model_application)

        context = {
            'utility_model_application' : utility_model_application,
            'form': form
        }

        return render(request, 'Utility_Model/edit_remarks.html', context)


    def post(self, request, slug):
        utility_model_application = get_object_or_404(UtilityModelApplicationModel, utility_model_slug=slug)

        form = EditRemarksForm(request.POST, instance=utility_model_application)

        if form.is_valid():
            form.save()
            return redirect('utility-model-detail', slug=utility_model_application.utility_model_slug)

        context = {
            'utility_model_application' : utility_model_application,
            'form': form
        }

        return render(request, 'Utility_Model/edit_remarks.html', context)


class AddSingleFile(LoginRequiredMixin, View):
    login_url = 'login'

    def get(self, request, slug, file_type):
        utility_model_application = get_object_or_404(UtilityModelApplicationModel, utility_model_slug=slug)

        draft_file = utility_model_application.draft_file.first()
        invention_pictures = utility_model_application.invention_pictures.first()
        abstract = utility_model_application.abstract_file.first()
        author_ids = utility_model_application.author_ids.first()
        memorandum_of_appointment = utility_model_application.memorandum_of_appointment.first()

        files = {
            'draft-file' : draft_file,
            'invention-pictures-file' : invention_pictures,
            'abstract-file' : abstract,
            'author-ids-file': author_ids,
            'memorandum-of-appointment-file' : memorandum_of_appointment
        }

        forms = {
            'draft-file' : DraftFileForm,
            'invention-pictures-file': InventionPicturesFileForm,
            'abstract-file' :AbstractFileForm,
            'author-ids-file': AuthorIdsFileForm,
            'memorandum-of-appointment-file' : MemorandumOfAppointmentFileForm
        }
        
        form = forms[file_type]
        file = files[file_type]

        if file is not None:
            return redirect('edit-file-utility-model', slug=utility_model_application.utility_model_slug, file_type=file_type)

        context = {
            'utility_model' : utility_model_application,
            'form' : form,
            'file_type' : file_type
        }
        
        return render(request, 'Utility_Model/new_file.html', context)


    def post(self, request, slug, file_type):
        utility_model_application = get_object_or_404(UtilityModelApplicationModel, utility_model_slug=slug)
        
        forms = {
            'draft-file' : DraftFileForm(request.POST, request.FILES),
            'invention-pictures-file': InventionPicturesFileForm(request.POST, request.FILES),
            'abstract-file' :AbstractFileForm(request.POST, request.FILES),
            'author-ids-file': AuthorIdsFileForm(request.POST, request.FILES),
            'memorandum-of-appointment-file' : MemorandumOfAppointmentFileForm(request.POST, request.FILES),
        }

        form = forms[file_type]
        
        if form.is_valid():
            new_file = form.save(commit=False)
            new_file.utility_model_application = utility_model_application
            utility_model_application.date_modified = new_file.date_modified
            utility_model_application.save()
            new_file.save()

            messages.success(request, 'A new file has been added successfully.')

            return redirect('utility-model-detail', slug=utility_model_application.utility_model_slug)
        
        context = {
            'utility_model' : utility_model_application,
            'form' : form,
            'file_type' : file_type
        }
        
        return render(request, 'Utility_Model/new_file.html', context)


class EditFile(LoginRequiredMixin, View):
    login_url = 'login'

    def get(self, request, slug, file_type):
        utility_model_application = get_object_or_404(UtilityModelApplicationModel, utility_model_slug=slug)

        draft_file = utility_model_application.draft_file.first()
        invention_pictures = utility_model_application.invention_pictures.first()
        abstract = utility_model_application.abstract_file.first()
        author_ids = utility_model_application.author_ids.first()
        memorandum_of_appointment = utility_model_application.memorandum_of_appointment.first()

        files = {
            'draft-file' : draft_file,
            'invention-pictures-file' : invention_pictures,
            'abstract-file' : abstract,
            'author-ids-file': author_ids,
            'memorandum-of-appointment-file' : memorandum_of_appointment
        }

        forms = {
            'draft-file' : DraftFileForm(instance=draft_file),
            'invention-pictures-file': InventionPicturesFileForm(instance=invention_pictures),
            'abstract-file' :AbstractFileForm(instance=abstract),
            'author-ids-file': AuthorIdsFileForm(instance=author_ids),
            'memorandum-of-appointment-file' : MemorandumOfAppointmentFileForm(instance=memorandum_of_appointment)
        }
        
        form = forms[file_type]
        file = files[file_type]

        if file == None:
            return redirect('new-file-utility-model', slug=utility_model_application.utility_model_slug, file_type=file_type)

        context = {
            'utility_model' : utility_model_application,
            'form' : form,
            'file_type' : file_type,
            'file' : file
        }
        
        return render(request, 'Utility_Model/edit_file.html', context)


    def post(self, request, slug, file_type):
        utility_model_application = get_object_or_404(UtilityModelApplicationModel, utility_model_slug=slug)

        draft_file = utility_model_application.draft_file.first()
        invention_pictures = utility_model_application.invention_pictures.first()
        abstract = utility_model_application.abstract_file.first()
        author_ids = utility_model_application.author_ids.first()
        memorandum_of_appointment = utility_model_application.memorandum_of_appointment.first()

        files = {
            'draft-file' : draft_file,
            'invention-pictures-file' : invention_pictures,
            'abstract-file' : abstract,
            'author-ids-file': author_ids,
            'memorandum-of-appointment-file' : memorandum_of_appointment
        }

        forms = {
            'draft-file' : DraftFileForm(request.POST, request.FILES, instance=draft_file),
            'invention-pictures-file': InventionPicturesFileForm(request.POST, request.FILES, instance=invention_pictures),
            'abstract-file' :AbstractFileForm(request.POST, request.FILES, instance=abstract),
            'author-ids-file': AuthorIdsFileForm(request.POST, request.FILES, instance=author_ids),
            'memorandum-of-appointment-file' : MemorandumOfAppointmentFileForm(request.POST, request.FILES, instance=memorandum_of_appointment)
        }
        
        form = forms[file_type]
        file = files[file_type]
        
        if 'Submit' in request.POST:
            if form.is_valid():
                new_file = form.save(commit=False)
                
                utility_model_application.date_modified = new_file.date_modified
                utility_model_application.save()

                new_file.save()

                messages.success(request, 'File has been succesfully updated.')

                return redirect('utility-model-detail', slug=utility_model_application.utility_model_slug)
        elif 'Delete' in request.POST:
            file.delete()

            messages.success(request, 'File has been succesfully deleted.')

            return redirect('utility-model-detail', slug=utility_model_application.utility_model_slug)


        context = {
            'utility_model' : utility_model_application,
            'form' : form,
            'file_type' : file_type,
            'file' : file
        }
        
        return render(request, 'Utility_Model/edit_file.html', context)


class DeleteWhole(LoginRequiredMixin, View):
    login_url = 'login'

    def get(self, request, slug):
        utility_model_application = get_object_or_404(UtilityModelApplicationModel, utility_model_slug=slug)
        
        draft_file = utility_model_application.draft_file.first()
        invention_pictures = utility_model_application.invention_pictures.first()
        abstract_file = utility_model_application.abstract_file.first()
        author_ids = utility_model_application.author_ids.first()
        memorandum_of_appointment = utility_model_application.memorandum_of_appointment.first()

        files = {
            'draft_file' : draft_file,
            'invention_pictures' : invention_pictures,
            'abstract_file' : abstract_file,
            'author_ids' : author_ids,
            'memorandum_of_appointment' :  memorandum_of_appointment,
        }


        context = {
            'utility_model' : utility_model_application,
            'file' :  files
        }

        return render(request, 'Utility_Model/delete_whole.html', context)


    def post(self, request, slug):
        utility_model_application = get_object_or_404(UtilityModelApplicationModel, utility_model_slug=slug)

        utility_model_application.delete()

        messages.success(request, 'Entry succesfully deleted.')

        return redirect('utility-model-home')
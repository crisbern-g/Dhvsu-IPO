from django.core.paginator import Paginator
from django.contrib import messages
from django.views import View
from django.shortcuts import redirect, render, get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import IndustrialDesignApplicationModel
from .forms import AddIndustrialDesignForm, EditRemarksForm, DraftFileForm, InventionPicturesFileForm, AbstractFileForm, AuthorIdsFileForm, MemorandumOfAppointmentFileForm
from django.db.models.functions import Lower

# Create your views here.
class IndustrialDesignHome(LoginRequiredMixin, View):
    login_url = 'login'

    def get(self, request):
        applications = IndustrialDesignApplicationModel.objects.all().order_by(Lower('application_name'))

        table_page = Paginator(applications, 20)
        current_page = request.GET.get('page')
        industrial_designs = table_page.get_page(current_page)

        context = {
            'industrial_designs' : industrial_designs
        }

        return render(request, 'Industrial_Design/home.html', context)


class SearchView(LoginRequiredMixin,View):
    login_url = 'login'

    def get(self, request):
        search_query = request.GET.get('search_query')

        applications = IndustrialDesignApplicationModel.objects.filter(application_name__contains=search_query)

        context = {
            'applications' : applications,
            'query' : search_query
        }

        return render(request, 'Industrial_Design/search_results.html', context)


class AddIndustrialDesignView(LoginRequiredMixin, View):
    login_url = 'login'

    def get(self, request):
        form = AddIndustrialDesignForm

        context = {
            'form' : form
        }

        return render(request, 'Industrial_Design/add.html', context)


    def post(self, request):
        form = AddIndustrialDesignForm(request.POST)

        if form.is_valid():
            new_application = form.save(commit=False)
            new_application.save()

            #return redirect('utility-model-detail', slug=new_application.slug)
            return redirect('industrial-design-detail', slug=new_application.slug)

        context = {
            'form' : form
        }

        return render(request, 'Industrial_Design/add.html', context)


class UtilityModelDetailView(LoginRequiredMixin, View):
    login_url= 'login'

    def get(self, request, slug):
        application = get_object_or_404(IndustrialDesignApplicationModel, slug=slug)

        draft_file = application.draft_file.first()
        invention_pictures = application.invention_pictures.first()
        abstract_file = application.abstract_file.first()
        author_ids = application.author_ids.first()
        memorandum_of_appointment = application.memorandum_of_appointment.first()

        documents = {
            'draft_file' : draft_file,
            'invention_pictures' : invention_pictures,
            'abstract_file' : abstract_file,
            'author_ids' : author_ids,
            'memorandum_of_appointment' :  memorandum_of_appointment,
        }

        context = {
            'documents' : documents,
            'application' : application
        }

        return render(request, 'Industrial_Design/detail.html', context)


class EditRemarks(LoginRequiredMixin, View):
    login_url = 'login'

    def get(self, request, slug):
        application = get_object_or_404(IndustrialDesignApplicationModel, slug=slug)

        form = EditRemarksForm(instance=application)

        context = {
            'application' : application,
            'form': form
        }

        return render(request, 'Industrial_Design/edit_remarks.html', context)


    def post(self, request, slug):
        application = get_object_or_404(IndustrialDesignApplicationModel, slug=slug)

        form = EditRemarksForm(request.POST, instance=application)

        if form.is_valid():
            form.save()
            return redirect('industrial-design-detail', slug=application.slug)

        context = {
            'application' : application,
            'form': form
        }

        return render(request, 'Industrial_Design/edit_remarks.html', context)


class AddSingleFile(LoginRequiredMixin, View):
    login_url = 'login'

    def get(self, request, slug, file_type):
        application = get_object_or_404(IndustrialDesignApplicationModel, slug=slug)

        draft_file = application.draft_file.first()
        invention_pictures = application.invention_pictures.first()
        abstract = application.abstract_file.first()
        author_ids = application.author_ids.first()
        memorandum_of_appointment = application.memorandum_of_appointment.first()

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
            return redirect('edit-file-industrial-design', slug=application.slug, file_type=file_type)

        context = {
            'application' : application,
            'form' : form,
            'file_type' : file_type
        }
        
        return render(request, 'Industrial_Design/new_file.html', context)


    def post(self, request, slug, file_type):
        application = get_object_or_404(IndustrialDesignApplicationModel, slug=slug)
        
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
            new_file.application = application
            application.date_modified = new_file.date_modified
            application.save()
            new_file.save()

            messages.success(request, 'A new file has been added successfully.')

            return redirect('industrial-design-detail', slug=application.slug)
        
        context = {
            'application' : application,
            'form' : form,
            'file_type' : file_type
        }
        
        return render(request, 'Industrial_Design/new_file.html', context)


class EditFile(LoginRequiredMixin, View):
    login_url = 'login'

    def get(self, request, slug, file_type):
        application = get_object_or_404(IndustrialDesignApplicationModel, slug=slug)

        draft_file = application.draft_file.first()
        invention_pictures = application.invention_pictures.first()
        abstract = application.abstract_file.first()
        author_ids = application.author_ids.first()
        memorandum_of_appointment = application.memorandum_of_appointment.first()

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
            return redirect('new-file-industrial-design', slug=application.slug, file_type=file_type)

        context = {
            'application' : application,
            'form' : form,
            'file_type' : file_type,
            'file' : file
        }
        
        return render(request, 'Industrial_Design/edit_file.html', context)


    def post(self, request, slug, file_type):
        application = get_object_or_404(IndustrialDesignApplicationModel, slug=slug)

        draft_file = application.draft_file.first()
        invention_pictures = application.invention_pictures.first()
        abstract = application.abstract_file.first()
        author_ids = application.author_ids.first()
        memorandum_of_appointment = application.memorandum_of_appointment.first()

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
                
                application.date_modified = new_file.date_modified
                application.save()

                new_file.save()

                messages.success(request, 'File has been succesfully updated.')

                return redirect('industrial-design-detail', slug=application.slug)
        elif 'Delete' in request.POST:
            file.delete()

            messages.success(request, 'File has been succesfully deleted.')

            return redirect('industrial-design-detail', slug=application.slug)


        context = {
            'application' : application,
            'form' : form,
            'file_type' : file_type,
            'file' : file
        }
        
        return render(request, 'Industrial_Design/edit_file.html', context)


class DeleteWhole(LoginRequiredMixin, View):
    login_url = 'login'

    def get(self, request, slug):
        application = get_object_or_404(IndustrialDesignApplicationModel, slug=slug)
        
        draft_file = application.draft_file.first()
        invention_pictures = application.invention_pictures.first()
        abstract_file = application.abstract_file.first()
        author_ids = application.author_ids.first()
        memorandum_of_appointment = application.memorandum_of_appointment.first()

        files = {
            'draft_file' : draft_file,
            'invention_pictures' : invention_pictures,
            'abstract_file' : abstract_file,
            'author_ids' : author_ids,
            'memorandum_of_appointment' :  memorandum_of_appointment,
        }


        context = {
            'application' : application,
            'file' :  files
        }

        return render(request, 'Industrial_Design/delete_whole.html', context)


    def post(self, request, slug):
        application = get_object_or_404(IndustrialDesignApplicationModel, slug=slug)

        application.delete()

        messages.success(request, 'Entry succesfully deleted.')

        return redirect('industrial-design-home')
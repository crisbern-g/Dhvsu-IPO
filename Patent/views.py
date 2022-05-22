import imp
from django.core.paginator import Paginator
from django.contrib import messages
from django.views import View
from django.shortcuts import redirect, render, get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import PatentApplicationModel
from .forms import AddPatentForm, EditRemarksForm, PatentDraftFileForm, InventionPicturesFileForm, AbstractFileForm, AuthorIdsFileForm, MemorandumOfAppointmentFileForm

# Create your views here.
class PatentHome(LoginRequiredMixin, View):
    login_url = 'login'

    def get(self, request):
        patent_applications = PatentApplicationModel.objects.all()

        table_page = Paginator(patent_applications, 20)
        current_page = request.GET.get('page')
        patents = table_page.get_page(current_page)

        context = {
            'patents' : patents
        }

        return render(request, 'Patent/patent_home.html', context)

class SearchView(LoginRequiredMixin,View):
    login_url = 'login'

    def get(self, request):
        search_query = request.GET.get('search_query')

        copyrights = PatentApplicationModel.objects.filter(patent_application_name__contains=search_query)

        context = {
            'patents' : copyrights,
            'query' : search_query
        }

        return render(request, 'Patent/search_results.html', context)


class AddPatentView(LoginRequiredMixin, View):
    login_url = 'login'

    def get(self, request):
        form = AddPatentForm()

        context = {
            'form' : form
        }

        return render(request, 'Patent/add_patent.html', context)


    def post(self, request):
        form = AddPatentForm(request.POST)

        if form.is_valid():
            new_patent = form.save(commit=False)
            new_patent.save()

            return redirect('patent-detail', slug=new_patent.patent_slug)

        context = {
            'form' : form
        }

        return render(request, 'Patent/add_patent.html', context)


class PatentDetailView(LoginRequiredMixin, View):
    login_url= 'login'

    def get(self, request, slug):
        patent_application = get_object_or_404(PatentApplicationModel, patent_slug=slug)

        patent_draft = patent_application.patent_draft.first()
        invention_pictures = patent_application.invention_pictures.first()
        abstract_file = patent_application.abstract_file.first()
        author_ids = patent_application.author_ids.first()
        memorandum_of_appointment = patent_application.memorandum_of_appointment.first()

        documents = {
            'patent_draft' : patent_draft,
            'invention_pictures' : invention_pictures,
            'abstract_file' : abstract_file,
            'author_ids' : author_ids,
            'memorandum_of_appointment' :  memorandum_of_appointment,
        }

        context = {
            'documents' : documents,
            'application' : patent_application
        }

        return render(request, 'Patent/patent_detail.html', context)


class EditRemarks(LoginRequiredMixin, View):
    login_url = 'login'

    def get(self, request, slug):
        patent_application = get_object_or_404(PatentApplicationModel, patent_slug=slug)

        form = EditRemarksForm(instance=patent_application)

        context = {
            'patent' : patent_application,
            'form': form
        }

        return render(request, 'Patent/edit_remarks.html', context)


    def post(self, request, slug):
        patent_application = get_object_or_404(PatentApplicationModel, patent_slug=slug)

        form = EditRemarksForm(request.POST, instance=patent_application)

        if form.is_valid():
            form.save()
            return redirect('patent-detail', slug=patent_application.patent_slug)

        context = {
            'patent' : patent_application,
            'form': form
        }

        return render(request, 'Patent/edit_remarks.html', context)


class AddSingleFile(LoginRequiredMixin, View):
    login_url = 'login'

    def get(self, request, slug, file_type):
        patent_application = get_object_or_404(PatentApplicationModel, patent_slug=slug)

        patent_draft = patent_application.patent_draft.first()
        invention_pictures = patent_application.invention_pictures.first()
        abstract = patent_application.abstract_file.first()
        author_ids = patent_application.author_ids.first()
        memorandum_of_appointment = patent_application.memorandum_of_appointment.first()

        files = {
            'patent-draft-file' : patent_draft,
            'invention-pictures-file' : invention_pictures,
            'abstract-file' : abstract,
            'author-ids-file': author_ids,
            'memorandum-of-appointment-file' : memorandum_of_appointment
        }

        forms = {
            'patent-draft-file' : PatentDraftFileForm,
            'invention-pictures-file': InventionPicturesFileForm,
            'abstract-file' :AbstractFileForm,
            'author-ids-file': AuthorIdsFileForm,
            'memorandum-of-appointment-file' : MemorandumOfAppointmentFileForm
        }
        
        form = forms[file_type]
        file = files[file_type]

        if file is not None:
            return redirect('edit-file-patent', slug=patent_application.patent_slug, file_type=file_type)

        context = {
            'patent' : patent_application,
            'form' : form,
            'file_type' : file_type
        }
        
        return render(request, 'Patent/new_file.html', context)


    def post(self, request, slug, file_type):
        patent_application = get_object_or_404(PatentApplicationModel, patent_slug=slug)

        forms = {
            'patent-draft-file' : PatentDraftFileForm(request.POST, request.FILES),
            'invention-pictures-file': InventionPicturesFileForm(request.POST, request.FILES),
            'abstract-file' : AbstractFileForm(request.POST, request.FILES),
            'author-ids-file': AuthorIdsFileForm(request.POST, request.FILES),
            'memorandum-of-appointment-file' : MemorandumOfAppointmentFileForm(request.POST, request.FILES),
        }
        
        form = forms[file_type]
        
        if form.is_valid():
            new_file = form.save(commit=False)
            new_file.patent_application = patent_application
            patent_application.date_modified = new_file.date_modified
            patent_application.save()
            new_file.save()

            messages.success(request, 'A new file has been added successfully.')

            return redirect('patent-detail', slug=patent_application.patent_slug)
        
        context = {
            'patent' : patent_application,
            'form' : form,
            'file_type' : file_type
        }
        
        return render(request, 'Patent/new_file.html', context)


class EditFile(LoginRequiredMixin, View):
    login_url = 'login'

    def get(self, request, slug, file_type):
        patent_application = get_object_or_404(PatentApplicationModel, patent_slug=slug)

        patent_draft = patent_application.patent_draft.first()
        invention_pictures = patent_application.invention_pictures.first()
        abstract = patent_application.abstract_file.first()
        author_ids = patent_application.author_ids.first()
        memorandum_of_appointment = patent_application.memorandum_of_appointment.first()

        files = {
            'patent-draft-file' : patent_draft,
            'invention-pictures-file' : invention_pictures,
            'abstract-file' : abstract,
            'author-ids-file': author_ids,
            'memorandum-of-appointment-file' : memorandum_of_appointment
        }

        forms = {
            'patent-draft-file' : PatentDraftFileForm(instance=patent_draft),
            'invention-pictures-file': InventionPicturesFileForm(instance=invention_pictures),
            'abstract-file' :AbstractFileForm(instance=abstract),
            'author-ids-file': AuthorIdsFileForm(instance=author_ids),
            'memorandum-of-appointment-file' : MemorandumOfAppointmentFileForm(instance=memorandum_of_appointment)
        }
        
        form = forms[file_type]
        file = files[file_type]

        if file == None:
            return redirect('new-file-patent', slug=slug, file_type=file_type)

        context = {
            'patent' : patent_application,
            'form' : form,
            'file_type' : file_type,
            'file' : file
        }
        
        return render(request, 'Patent/edit_file.html', context)


    def post(self, request, slug, file_type):
        patent_application = get_object_or_404(PatentApplicationModel, patent_slug=slug)

        patent_draft = patent_application.patent_draft.first()
        invention_pictures = patent_application.invention_pictures.first()
        abstract = patent_application.abstract_file.first()
        author_ids = patent_application.author_ids.first()
        memorandum_of_appointment = patent_application.memorandum_of_appointment.first()

        files = {
            'patent-draft-file' : patent_draft,
            'invention-pictures-file' : invention_pictures,
            'abstract-file' : abstract,
            'author-ids-file': author_ids,
            'memorandum-of-appointment-file' : memorandum_of_appointment
        }

        forms = {
            'patent-draft-file' : PatentDraftFileForm(request.POST, request.FILES,instance=patent_draft),
            'invention-pictures-file': InventionPicturesFileForm(request.POST, request.FILES,instance=invention_pictures),
            'abstract-file' :AbstractFileForm(request.POST, request.FILES,instance=abstract),
            'author-ids-file': AuthorIdsFileForm(request.POST, request.FILES,instance=author_ids),
            'memorandum-of-appointment-file' : MemorandumOfAppointmentFileForm(request.POST, request.FILES,instance=memorandum_of_appointment)
        }
        
        form = forms[file_type]
        file = files[file_type]
        
        if 'Submit' in request.POST:
            if form.is_valid():
                new_file = form.save(commit=False)
                
                patent_application.date_modified = new_file.date_modified
                patent_application.save()

                new_file.save()

                messages.success(request, 'File has been succesfully updated.')

                return redirect('patent-detail', slug=patent_application.patent_slug)
        elif 'Delete' in request.POST:
            file.delete()

            messages.success(request, 'File has been succesfully deleted.')

            return redirect('patent-detail', slug=patent_application.patent_slug)


        context = {
            'patent' : patent_application,
            'form' : form,
            'file_type' : file_type,
            'file' : file
        }

        return render(request, 'Patent/edit_file.html', context)


class DeleteWhole(LoginRequiredMixin, View):
    login_url = 'login'

    def get(self, request, slug):
        patent_application = get_object_or_404(PatentApplicationModel, patent_slug=slug)
        
        patent_draft = patent_application.patent_draft.first()
        invention_pictures = patent_application.invention_pictures.first()
        abstract_file = patent_application.abstract_file.first()
        author_ids = patent_application.author_ids.first()
        memorandum_of_appointment = patent_application.memorandum_of_appointment.first()

        files = {
            'patent_draft' : patent_draft,
            'invention_pictures' : invention_pictures,
            'abstract_file' : abstract_file,
            'author_ids' : author_ids,
            'memorandum_of_appointment' :  memorandum_of_appointment,
        }


        context = {
            'patent' : patent_application,
            'file' :  files
        }

        return render(request, 'Patent/delete_whole.html', context)


    def post(self, request, slug):
        patent_application = get_object_or_404(PatentApplicationModel, patent_slug=slug)

        patent_application.delete()

        messages.success(request, 'Entry succesfully deleted.')

        return redirect('patent-home')
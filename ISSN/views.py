from django.core.paginator import Paginator
from django.contrib import messages
from django.views import View
from django.shortcuts import redirect, render, get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import IssnApplicationModel
from .forms import AddIssnApplicationForm, EditRemarksForm, JournalForm, EditorialForm, AuthorIdsFileForm, MemorandumOfAppointmentFileForm
from django.db.models.functions import Lower

# Create your views here.
class IssnHome(LoginRequiredMixin, View):
    login_url = 'login'

    def get(self, request):
        applications = IssnApplicationModel.objects.all().order_by(Lower('application_name'))

        table_page = Paginator(applications, 20)
        current_page = request.GET.get('page')
        issns = table_page.get_page(current_page)

        context = {
            'issns' : issns
        }

        return render(request, 'ISSN/home.html', context)


class SearchView(LoginRequiredMixin,View):
    login_url = 'login'

    def get(self, request):
        search_query = request.GET.get('search_query')

        applications = IssnApplicationModel.objects.filter(application_name__contains=search_query)

        context = {
            'applications' : applications,
            'query' : search_query
        }

        return render(request, 'ISSN/search_results.html', context)


class AddIssnView(LoginRequiredMixin, View):
    login_url = 'login'

    def get(self, request):
        form = AddIssnApplicationForm

        context = {
            'form' : form
        }

        return render(request, 'ISSN/add.html', context)


    def post(self, request):
        form = AddIssnApplicationForm(request.POST)

        if form.is_valid():
            new_application = form.save(commit=False)
            new_application.save()

            return redirect('issn-detail', slug=new_application.slug)

        context = {
            'form' : form
        }

        return render(request, 'ISSN/add.html', context)


class IssnDetailView(LoginRequiredMixin, View):
    login_url= 'login'

    def get(self, request, slug):
        application = get_object_or_404(IssnApplicationModel, slug=slug)

        journal = application.journal.first()
        editorial = application.editorial.first()
        author_ids = application.author_ids.first()
        memorandum_of_appointment = application.memorandum_of_appointment.first()

        documents = {
            'journal': journal,
            'editorial' : editorial,
            'author_ids' : author_ids,
            'memorandum_of_appointment' :  memorandum_of_appointment,
        }

        context = {
            'documents' : documents,
            'application' : application
        }

        return render(request, 'ISSN/detail.html', context)


class EditRemarks(LoginRequiredMixin, View):
    login_url = 'login'

    def get(self, request, slug):
        application = get_object_or_404(IssnApplicationModel, slug=slug)

        form = EditRemarksForm(instance=application)

        context = {
            'application' : application,
            'form': form
        }

        return render(request, 'ISSN/edit_remarks.html', context)


    def post(self, request, slug):
        application = get_object_or_404(IssnApplicationModel, slug=slug)

        form = EditRemarksForm(request.POST, instance=application)

        if form.is_valid():
            form.save()
            return redirect('issn-detail', slug=application.slug)

        context = {
            'application' : application,
            'form': form
        }

        return render(request, 'ISSN/edit_remarks.html', context)


class AddSingleFile(LoginRequiredMixin, View):
    login_url = 'login'

    def get(self, request, slug, file_type):
        application = get_object_or_404(IssnApplicationModel, slug=slug)

        journal = application.journal.first()
        editorial = application.editorial.first()
        author_ids = application.author_ids.first()
        memorandum_of_appointment = application.memorandum_of_appointment.first()

        files = {
            'journal' : journal,
            'editorial' : editorial,
            'author-ids-file': author_ids,
            'memorandum-of-appointment-file' : memorandum_of_appointment
        }

        forms = {
            'journal' : JournalForm,
            'editorial': EditorialForm,
            'author-ids-file': AuthorIdsFileForm,
            'memorandum-of-appointment-file' : MemorandumOfAppointmentFileForm
        }
        
        form = forms[file_type]
        file = files[file_type]

        if file is not None:
            return redirect('edit-file-issn', slug=application.slug, file_type=file_type)

        context = {
            'application' : application,
            'form' : form,
            'file_type' : file_type
        }
        
        return render(request, 'ISSN/new_file.html', context)


    def post(self, request, slug, file_type):
        application = get_object_or_404(IssnApplicationModel, slug=slug)
        
        forms = {
            'journal' : JournalForm(request.POST, request.FILES),
            'editorial': EditorialForm(request.POST, request.FILES),
            'author-ids-file': AuthorIdsFileForm(request.POST, request.FILES),
            'memorandum-of-appointment-file' : MemorandumOfAppointmentFileForm(request.POST, request.FILES)
        }

        form = forms[file_type]
        
        if form.is_valid():
            new_file = form.save(commit=False)
            new_file.application = application
            application.date_modified = new_file.date_modified
            application.save()
            new_file.save()

            messages.success(request, 'A new file has been added successfully.')

            return redirect('issn-detail', slug=application.slug)
        
        context = {
            'application' : application,
            'form' : form,
            'file_type' : file_type
        }
        
        return render(request, 'ISSN/new_file.html', context)


class EditFile(LoginRequiredMixin, View):
    login_url = 'login'

    def get(self, request, slug, file_type):
        application = get_object_or_404(IssnApplicationModel, slug=slug)

        journal = application.journal.first()
        editorial = application.editorial.first()
        author_ids = application.author_ids.first()
        memorandum_of_appointment = application.memorandum_of_appointment.first()

        files = {
            'journal' : journal,
            'editorial' : editorial,
            'author-ids-file': author_ids,
            'memorandum-of-appointment-file' : memorandum_of_appointment
        }

        forms = {
            'journal' : JournalForm(instance=journal),
            'editorial': EditorialForm(instance=editorial),
            'author-ids-file': AuthorIdsFileForm(instance=author_ids),
            'memorandum-of-appointment-file' : MemorandumOfAppointmentFileForm(instance=memorandum_of_appointment)
        }
        
        form = forms[file_type]
        file = files[file_type]

        if file == None:
            return redirect('new-file-issn', slug=application.slug, file_type=file_type)

        context = {
            'application' : application,
            'form' : form,
            'file_type' : file_type,
            'file' : file
        }
        
        return render(request, 'ISSN/edit_file.html', context)


    def post(self, request, slug, file_type):
        application = get_object_or_404(IssnApplicationModel, slug=slug)

        journal = application.journal.first()
        editorial = application.editorial.first()
        author_ids = application.author_ids.first()
        memorandum_of_appointment = application.memorandum_of_appointment.first()

        files = {
            'journal' : journal,
            'editorial' : editorial,
            'author-ids-file': author_ids,
            'memorandum-of-appointment-file' : memorandum_of_appointment
        }

        forms = {
            'journal' : JournalForm(request.POST, request.FILES, instance=journal),
            'editorial': EditorialForm(request.POST, request.FILES, instance=editorial),
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

                return redirect('issn-detail', slug=application.slug)
        elif 'Delete' in request.POST:
            file.delete()

            messages.success(request, 'File has been succesfully deleted.')

            return redirect('issn-detail', slug=application.slug)


        context = {
            'application' : application,
            'form' : form,
            'file_type' : file_type,
            'file' : file
        }
        
        return render(request, 'ISSN/edit_file.html', context)


class DeleteWhole(LoginRequiredMixin, View):
    login_url = 'login'

    def get(self, request, slug):
        application = get_object_or_404(IssnApplicationModel, slug=slug)
        
        journal = application.journal.first()
        editorial = application.editorial.first()
        author_ids = application.author_ids.first()
        memorandum_of_appointment = application.memorandum_of_appointment.first()

        files = {
            'journal' : journal,
            'editorial' : editorial,
            'author_ids' : author_ids,
            'memorandum_of_appointment' :  memorandum_of_appointment,
        }


        context = {
            'application' : application,
            'file' :  files
        }

        return render(request, 'ISSN/delete_whole.html', context)


    def post(self, request, slug):
        application = get_object_or_404(IssnApplicationModel, slug=slug)

        application.delete()

        messages.success(request, 'Entry succesfully deleted.')

        return redirect('issn-home')
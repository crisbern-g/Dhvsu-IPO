from django.core.paginator import Paginator
from django.contrib import messages
from django.views import View
from django.shortcuts import redirect, render, get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import TrademarkApplicationModel
from .forms import AddTrademarkApplicationForm, EditRemarksForm, ApplicationFormForm, MarkFileForm, AuthorIdsFileForm, MemorandumOfAppointmentFileForm
from django.db.models.functions import Lower


# Create your views here.
class TrademarkHome(LoginRequiredMixin, View):
    login_url = 'login'

    def get(self, request):
        applications = TrademarkApplicationModel.objects.all().order_by(Lower('application_name'))

        table_page = Paginator(applications, 20)
        current_page = request.GET.get('page')
        trademarks = table_page.get_page(current_page)

        context = {
            'trademarks' : trademarks
        }

        return render(request, 'Trademark/home.html', context)


class SearchView(LoginRequiredMixin,View):
    login_url = 'login'

    def get(self, request):
        search_query = request.GET.get('search_query')

        applications = TrademarkApplicationModel.objects.filter(application_name__contains=search_query)

        context = {
            'applications' : applications,
            'query' : search_query
        }

        return render(request, 'Trademark/search_results.html', context)


class AddTrademarkView(LoginRequiredMixin, View):
    login_url = 'login'

    def get(self, request):
        form = AddTrademarkApplicationForm

        context = {
            'form' : form
        }

        return render(request, 'Trademark/add.html', context)


    def post(self, request):
        form = AddTrademarkApplicationForm(request.POST)

        if form.is_valid():
            new_application = form.save(commit=False)
            new_application.save()

            return redirect('trademark-detail', slug=new_application.slug)

        context = {
            'form' : form
        }

        return render(request, 'Trademark/add.html', context)


class TrademarkDetailView(LoginRequiredMixin, View):
    login_url= 'login'

    def get(self, request, slug):
        application = get_object_or_404(TrademarkApplicationModel, slug=slug)

        application_form = application.application_form.first()
        mark = application.mark.first()
        author_ids = application.author_ids.first()
        memorandum_of_appointment = application.memorandum_of_appointment.first()

        documents = {
            'application_form': application_form,
            'mark' : mark,
            'author_ids' : author_ids,
            'memorandum_of_appointment' :  memorandum_of_appointment,
        }

        context = {
            'documents' : documents,
            'application' : application
        }

        return render(request, 'Trademark/detail.html', context)


class EditRemarks(LoginRequiredMixin, View):
    login_url = 'login'

    def get(self, request, slug):
        application = get_object_or_404(TrademarkApplicationModel, slug=slug)

        form = EditRemarksForm(instance=application)

        context = {
            'application' : application,
            'form': form
        }

        return render(request, 'Trademark/edit_remarks.html', context)


    def post(self, request, slug):
        application = get_object_or_404(TrademarkApplicationModel, slug=slug)

        form = EditRemarksForm(request.POST, instance=application)

        if form.is_valid():
            form.save()
            return redirect('trademark-detail', slug=application.slug)

        context = {
            'application' : application,
            'form': form
        }

        return render(request, 'Trademark/edit_remarks.html', context)


class AddSingleFile(LoginRequiredMixin, View):
    login_url = 'login'

    def get(self, request, slug, file_type):
        application = get_object_or_404(TrademarkApplicationModel, slug=slug)

        application_form = application.application_form.first()
        mark = application.mark.first()
        author_ids = application.author_ids.first()
        memorandum_of_appointment = application.memorandum_of_appointment.first()

        files = {
            'application-form' : application_form,
            'mark' : mark,
            'author-ids-file': author_ids,
            'memorandum-of-appointment-file' : memorandum_of_appointment
        }

        forms = {
            'application-form' : ApplicationFormForm,
            'mark': MarkFileForm,
            'author-ids-file': AuthorIdsFileForm,
            'memorandum-of-appointment-file' : MemorandumOfAppointmentFileForm
        }
        
        form = forms[file_type]
        file = files[file_type]

        if file is not None:
            return redirect('edit-file-trademark', slug=application.slug, file_type=file_type)

        context = {
            'application' : application,
            'form' : form,
            'file_type' : file_type
        }
        
        return render(request, 'Trademark/new_file.html', context)


    def post(self, request, slug, file_type):
        application = get_object_or_404(TrademarkApplicationModel, slug=slug)
        
        forms = {
            'application-form' : ApplicationFormForm(request.POST, request.FILES),
            'mark': MarkFileForm(request.POST, request.FILES),
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

            return redirect('trademark-detail', slug=application.slug)
        
        context = {
            'application' : application,
            'form' : form,
            'file_type' : file_type
        }
        
        return render(request, 'Trademark/new_file.html', context)


class EditFile(LoginRequiredMixin, View):
    login_url = 'login'

    def get(self, request, slug, file_type):
        application = get_object_or_404(TrademarkApplicationModel, slug=slug)

        application_form = application.application_form.first()
        mark = application.mark.first()
        author_ids = application.author_ids.first()
        memorandum_of_appointment = application.memorandum_of_appointment.first()

        files = {
            'application-form' : application_form,
            'mark' : mark,
            'author-ids-file': author_ids,
            'memorandum-of-appointment-file' : memorandum_of_appointment
        }

        forms = {
            'application-form' : ApplicationFormForm(instance=application_form),
            'mark': MarkFileForm(instance=mark),
            'author-ids-file': AuthorIdsFileForm(instance=author_ids),
            'memorandum-of-appointment-file' : MemorandumOfAppointmentFileForm(instance=memorandum_of_appointment)
        }
        
        form = forms[file_type]
        file = files[file_type]

        if file == None:
            return redirect('new-file-trademark', slug=application.slug, file_type=file_type)

        context = {
            'application' : application,
            'form' : form,
            'file_type' : file_type,
            'file' : file
        }
        
        return render(request, 'Trademark/edit_file.html', context)


    def post(self, request, slug, file_type):
        application = get_object_or_404(TrademarkApplicationModel, slug=slug)

        application_form = application.application_form.first()
        mark = application.mark.first()
        author_ids = application.author_ids.first()
        memorandum_of_appointment = application.memorandum_of_appointment.first()

        files = {
            'application-form' : application_form,
            'mark' : mark,
            'author-ids-file': author_ids,
            'memorandum-of-appointment-file' : memorandum_of_appointment
        }

        forms = {
            'application-form' : ApplicationFormForm(request.POST, request.FILES, instance=application_form),
            'mark': MarkFileForm(request.POST, request.FILES, instance=mark),
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

                return redirect('trademark-detail', slug=application.slug)
        elif 'Delete' in request.POST:
            file.delete()

            messages.success(request, 'File has been succesfully deleted.')

            return redirect('trademark-detail', slug=application.slug)


        context = {
            'application' : application,
            'form' : form,
            'file_type' : file_type,
            'file' : file
        }
        
        return render(request, 'Trademark/edit_file.html', context)


class DeleteWhole(LoginRequiredMixin, View):
    login_url = 'login'

    def get(self, request, slug):
        application = get_object_or_404(TrademarkApplicationModel, slug=slug)
        
        application_form = application.application_form.first()
        mark = application.mark.first()
        author_ids = application.author_ids.first()
        memorandum_of_appointment = application.memorandum_of_appointment.first()

        files = {
            'application_form' : application_form,
            'mark' : mark,
            'author_ids' : author_ids,
            'memorandum_of_appointment' :  memorandum_of_appointment,
        }


        context = {
            'application' : application,
            'file' :  files
        }

        return render(request, 'Trademark/delete_whole.html', context)


    def post(self, request, slug):
        application = get_object_or_404(TrademarkApplicationModel, slug=slug)

        application.delete()

        messages.success(request, 'Entry succesfully deleted.')

        return redirect('trademark-home')
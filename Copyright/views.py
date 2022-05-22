from django.core.paginator import Paginator
from django.contrib import messages
from django.views import View
from django.shortcuts import redirect, render, get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import CopyRightApplicationModel
from .forms import AddCopyrightForm, AddCopyrightApplicationFileForm, AddDeedOfAssignmentFileForm, ElectronicCopyFileForm, AuthorIdsFileForm, MemorandumOfAppointmentFileForm, CertificateOfRegistrationFileForm, EditRemarksForm


# Create your views here.
class CopyrightHome(LoginRequiredMixin, View):
    login_url='login'

    def get(self, request):
        copyright_applications = CopyRightApplicationModel.objects.all()

        table_page = Paginator(copyright_applications, 10)
        current_page = request.GET.get('page')
        copyrights = table_page.get_page(current_page)

        context = {
            'copyrights' : copyrights
        }

        return render(request, 'Copyright/copyright_home.html', context)


class SearchView(LoginRequiredMixin,View):
    login_url = 'login'

    def get(self, request):
        search_query = request.GET.get('search_query')

        copyrights = CopyRightApplicationModel.objects.filter(copyright_application_name__contains=search_query)
        
        print(copyrights)

        context = {
            'copyrights' : copyrights,
            'query' : search_query
        }

        return render(request, 'Copyright/search_results.html', context)


class AddCopyrightView(LoginRequiredMixin, View):
    login_url='login'

    def get(self, request):
        form = AddCopyrightForm()

        context = {
            'form' : form
        }

        return render(request, 'Copyright/add_copyright.html', context)


    def post(self, request):
        form = AddCopyrightForm(request.POST)

        if form.is_valid():
            new_copyright = form.save(commit=False)
            new_copyright.save()

            return redirect('copyright-detail', slug=new_copyright.copyright_slug)

        context = {
            'form' : form
        }

        return render(request, 'Copyright/add_copyright.html', context)


class EditRemarks(LoginRequiredMixin, View):
    login_url = 'login'

    def get(self, request, slug):
        copyright_application = get_object_or_404(CopyRightApplicationModel, copyright_slug=slug)

        form = EditRemarksForm(instance=copyright_application)

        context = {
            'copyright' : copyright_application,
            'form': form
        }

        return render(request, 'Copyright/edit_remarks.html', context)


    def post(self, request, slug):
        copyright_application = get_object_or_404(CopyRightApplicationModel, copyright_slug=slug)

        form = EditRemarksForm(request.POST, instance=copyright_application)

        if form.is_valid():
            
            form.save()

            return redirect('copyright-detail', slug=copyright_application.copyright_slug)

        context = {
            'copyright' : copyright_application,
            'form': form
        }

        return render(request, 'Copyright/edit_remarks.html', context)


class CopyrightDetailView(LoginRequiredMixin, View):
    login_url= 'login'

    def get(self, request, slug):
        copyright_application = get_object_or_404(CopyRightApplicationModel, copyright_slug=slug)

        copyright_application_file = copyright_application.copyright_application.first()
        deed_of_assignment_file  = copyright_application.deed_of_assignment.first()
        electronic_copy_file = copyright_application.electronic_copy.first()
        author_ids = copyright_application.author_ids.first()
        memorandum_of_appointment_file = copyright_application.memorandum_of_appointment.first()
        certificate_of_registration_file = copyright_application.certificate_of_registration.first()


        documents = {
            'application_file' : copyright_application_file,
            'deed_of_assignment_file' : deed_of_assignment_file,
            'electronic_copy_file' : electronic_copy_file,
            'author_ids_file' : author_ids,
            'memorandum_of_appointment_file' :  memorandum_of_appointment_file,
            'certificate_of_registration_file' :certificate_of_registration_file
        }


        context = {
            'documents' : documents,
            'application' : copyright_application
        }

        return render(request, 'Copyright/copyright_detail.html', context)


class AddSingleFile(LoginRequiredMixin, View):
    login_url = 'login'

    def get(self, request, slug, file_type):
        copyright_application = get_object_or_404(CopyRightApplicationModel, copyright_slug=slug)

        application_file = copyright_application.copyright_application.first()
        deed_of_assignment = copyright_application.deed_of_assignment.first()
        electronic_copy = copyright_application.electronic_copy.first()
        author_ids = copyright_application.author_ids.first()
        memorandum_of_appointment = copyright_application.memorandum_of_appointment.first()
        certificate_of_registration = copyright_application.certificate_of_registration.first()

        files = {
            'application-file' : application_file,
            'deed-of-assignment' : deed_of_assignment,
            'electronic-copy' : electronic_copy,
            'author-ids' : author_ids,
            'memorandum-of-appointment' :  memorandum_of_appointment,
            'certificate-of-registration' : certificate_of_registration,
        }

        forms = {
            'application-file' : AddCopyrightApplicationFileForm(),
            'deed-of-assignment' : AddDeedOfAssignmentFileForm(),
            'electronic-copy' : ElectronicCopyFileForm(),
            'author-ids' : AuthorIdsFileForm(),
            'memorandum-of-appointment' :  MemorandumOfAppointmentFileForm(),
            'certificate-of-registration' : CertificateOfRegistrationFileForm()
        }
        
        form = forms[file_type]
        file = files[file_type]

        if file is not None:
            return redirect('edit-file', slug=copyright_application.copyright_slug, file_type=file_type)

        context = {
            'copyright' : copyright_application,
            'form' : form,
            'file_type' : file_type
        }
        
        return render(request, 'Copyright/new_file.html', context)


    def post(self, request, slug, file_type):
        copyright_application = get_object_or_404(CopyRightApplicationModel, copyright_slug=slug)

        forms = {
            'application-file' : AddCopyrightApplicationFileForm(request.POST, request.FILES),
            'deed-of-assignment' : AddDeedOfAssignmentFileForm(request.POST, request.FILES),
            'electronic-copy' : ElectronicCopyFileForm(request.POST, request.FILES),
            'author-ids' : AuthorIdsFileForm(request.POST, request.FILES),
            'memorandum-of-appointment' :  MemorandumOfAppointmentFileForm(request.POST, request.FILES),
            'certificate-of-registration' : CertificateOfRegistrationFileForm(request.POST, request.FILES)
        }
        
        form = forms[file_type]
        
        if form.is_valid():
            new_file = form.save(commit=False)
            new_file.copyright_application = copyright_application
            copyright_application.date_modified = new_file.date_modified
            copyright_application.save()
            new_file.save()

            messages.success(request, 'A new file has been added successfully.')

            return redirect('copyright-detail', slug=copyright_application.copyright_slug)
        
        context = {
            'copyright' : copyright_application,
            'form' : form,
            'file_type' : file_type
        }

        return render(request, 'Copyright/new_file.html', context)


class EditFile(LoginRequiredMixin, View):
    login_url = 'login'

    def get(self, request, slug, file_type):
        copyright_application = get_object_or_404(CopyRightApplicationModel, copyright_slug=slug)

        application_file = copyright_application.copyright_application.first()
        deed_of_assignment = copyright_application.deed_of_assignment.first()
        electronic_copy = copyright_application.electronic_copy.first()
        author_ids = copyright_application.author_ids.first()
        memorandum_of_appointment = copyright_application.memorandum_of_appointment.first()
        certificate_of_registration = copyright_application.certificate_of_registration.first()

        files = {
            'application-file' : application_file,
            'deed-of-assignment' : deed_of_assignment,
            'electronic-copy' : electronic_copy,
            'author-ids' : author_ids,
            'memorandum-of-appointment' :  memorandum_of_appointment,
            'certificate-of-registration' : certificate_of_registration,
        }

        forms = {
            'application-file' : AddCopyrightApplicationFileForm(instance=application_file),
            'deed-of-assignment' : AddDeedOfAssignmentFileForm(instance=deed_of_assignment),
            'electronic-copy' : ElectronicCopyFileForm(instance=electronic_copy),
            'author-ids' : AuthorIdsFileForm(instance=author_ids),
            'memorandum-of-appointment' :  MemorandumOfAppointmentFileForm(instance=memorandum_of_appointment),
            'certificate-of-registration' : CertificateOfRegistrationFileForm(instance=certificate_of_registration)
        }

        form = forms[file_type]
        file = files[file_type]

        if file == None:
            return redirect('new-file', slug=slug, file_type=file_type)

        context = {
            'copyright' : copyright_application,
            'form' : form,
            'file_type' : file_type,
            'file' : file
        }
        
        return render(request, 'Copyright/edit_file.html', context)


    def post(self, request, slug, file_type):
        copyright_application = get_object_or_404(CopyRightApplicationModel, copyright_slug=slug)

        application_file = copyright_application.copyright_application.first()
        deed_of_assignment = copyright_application.deed_of_assignment.first()
        electronic_copy = copyright_application.electronic_copy.first()
        author_ids = copyright_application.author_ids.first()
        memorandum_of_appointment = copyright_application.memorandum_of_appointment.first()
        certificate_of_registration = copyright_application.certificate_of_registration.first()

        files = {
            'application-file' : application_file,
            'deed-of-assignment' : deed_of_assignment,
            'electronic-copy' : electronic_copy,
            'author-ids' : author_ids,
            'memorandum-of-appointment' :  memorandum_of_appointment,
            'certificate-of-registration' : certificate_of_registration,
        }

        forms = {
            'application-file' : AddCopyrightApplicationFileForm(request.POST, request.FILES, instance=application_file),
            'deed-of-assignment' : AddDeedOfAssignmentFileForm(request.POST, request.FILES, instance=deed_of_assignment),
            'electronic-copy' : ElectronicCopyFileForm(request.POST, request.FILES, instance=electronic_copy),
            'author-ids' : AuthorIdsFileForm(request.POST, request.FILES, instance=author_ids),
            'memorandum-of-appointment' :  MemorandumOfAppointmentFileForm(request.POST, request.FILES, instance=memorandum_of_appointment),
            'certificate-of-registration' : CertificateOfRegistrationFileForm(request.POST, request.FILES, instance=certificate_of_registration)
        }
        
        form = forms[file_type]
        file = files[file_type]
        
        if 'Submit' in request.POST:
            if form.is_valid():
                new_file = form.save(commit=False)
                
                copyright_application.date_modified = new_file.date_modified
                copyright_application.save()

                new_file.save()

                messages.success(request, 'File has been succesfully updated.')

                return redirect('copyright-detail', slug=copyright_application.copyright_slug)
        elif 'Delete' in request.POST:
            file.delete()

            messages.success(request, 'File has been succesfully deleted.')

            return redirect('copyright-detail', slug=copyright_application.copyright_slug)


        context = {
            'copyright' : copyright_application,
            'form' : form,
            'file_type' : file_type,
            'file' : file
        }

        return render(request, 'Copyright/edit_file.html', context)


class DeleteWhole(LoginRequiredMixin, View):
    login_url = 'login'

    def get(self, request, slug):
        copyright_application = get_object_or_404(CopyRightApplicationModel, copyright_slug=slug)
        
        application_file = copyright_application.copyright_application.first()
        deed_of_assignment = copyright_application.deed_of_assignment.first()
        electronic_copy = copyright_application.electronic_copy.first()
        author_ids = copyright_application.author_ids.first()
        memorandum_of_appointment = copyright_application.memorandum_of_appointment.first()
        certificate_of_registration = copyright_application.certificate_of_registration.first()

        files = {
            'application_file' : application_file,
            'deed_of_assignment' : deed_of_assignment,
            'electronic_copy' : electronic_copy,
            'author_ids' : author_ids,
            'memorandum_of_appointment' :  memorandum_of_appointment,
            'certificate_of_registration' : certificate_of_registration,
        }

        context = {
            'copyright' : copyright_application,
            'file' :  files
        }

        return render(request, 'Copyright/delete_whole.html', context)


    def post(self, request, slug):
        copyright_application = get_object_or_404(CopyRightApplicationModel, copyright_slug=slug)

        copyright_application.delete()

        messages.success(request, 'Entry succesfully deleted.')

        return redirect('copyright-home')
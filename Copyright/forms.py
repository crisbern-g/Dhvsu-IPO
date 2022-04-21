from pyexpat import model
from statistics import mode
from django import forms
from .models import CopyRightApplicationModel, CopyrightApplicationFileModel, DeedOfAssignmentFileModel, ElectronicCopyFileModel, AuthorIdsFileModel, MemorandumOfAppointmentFileModel, CertificateOfRegistrationFileModel

class AddCopyrightForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.label_suffix = ""

    class Meta:
        model = CopyRightApplicationModel
        exclude = ('copyright_slug',)

        labels = {
            'copyright_application_name' : 'Name',
            'Remarks' : 'Remarks'
        }


class EditRemarksForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.label_suffix = ""

    class Meta:
        model = CopyRightApplicationModel
        exclude = ('copyright_slug', 'copyright_application_name')

        labels = {
            'Remarks' : 'Remarks'
        }

class AddCopyrightApplicationFileForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.label_suffix = ""


    class Meta:
        model = CopyrightApplicationFileModel
        exclude =('copyright_application',)

        labels = {
            'application_file' : 'Application',
        }

        widgets = {
            'application_file' : forms.FileInput(attrs={'accept' : '.pdf,.zip'})
        }


class AddDeedOfAssignmentFileForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.label_suffix = ""

    class Meta:
        model = DeedOfAssignmentFileModel
        exclude =('copyright_application',)

        labels = {
            'deed_of_assignment_file' : 'Deed of Assignment',
        }

        widgets = {
            'deed_of_assignment_file' : forms.FileInput(attrs={'accept' : '.pdf,.zip'})
        }


class ElectronicCopyFileForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.label_suffix = ""


    class Meta:
        model = ElectronicCopyFileModel
        exclude =('copyright_application',)

        labels = {
            'electronic_copy_file' : 'Electronic Copy of the Work'
        }

        widgets = {
            'electronic_copy_file' : forms.FileInput(attrs={'accept' : '.pdf,.zip'})
        }


class AuthorIdsFileForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.label_suffix = ""


    class Meta:
        model = AuthorIdsFileModel
        exclude =('copyright_application',)

        labels = {
            'author_ids_file' : 'ID(s) of the Author(s)'
        }

        widgets = {
            'author_ids_file' : forms.FileInput(attrs={'accept' : '.pdf,.zip'})
        }
        



class MemorandumOfAppointmentFileForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.label_suffix = ""


    class Meta:
        model = MemorandumOfAppointmentFileModel
        exclude =('copyright_application',)

        labels = {
            'memorandum_of_appointment_file' : 'Memorandum of Appointment/Certificate of Employment'
        }

        widgets = {
            'memorandum_of_appointment_file' : forms.FileInput(attrs={'accept' : '.pdf,.zip'})
        }


class CertificateOfRegistrationFileForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.label_suffix = ""


    class Meta:
        model = CertificateOfRegistrationFileModel
        exclude =('copyright_application',)

        labels = {
            'certificate_of_registration_file' : 'Certificate of Registration'
        }

        widgets = {
            'certificate_of_registration_file' : forms.FileInput(attrs={'accept' : '.pdf,.zip'})
        }

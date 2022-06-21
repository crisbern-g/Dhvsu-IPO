from django import forms
from .models import IssnApplicationModel, JournalModel, EditorialModel, AuthorIdsFileModel, MemorandumOfAppointmentFileModel


class AddIssnApplicationForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.label_suffix = ""

    class Meta:
        model = IssnApplicationModel
        exclude = ('slug',)

        labels = {
            'application_name' : 'Name',
            'remarks' : 'Remarks'
        }


class EditRemarksForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.label_suffix = ""

    class Meta:
        model = IssnApplicationModel
        exclude = ('slug', 'application_name')

        labels = {
            'Remarks' : 'Remarks'
        }


class JournalForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.label_suffix = ""


    class Meta:
        model = JournalModel
        exclude =('application',)

        labels = {
            'journal_file' : 'Copy of the Journal',
        }

        widgets = {
            'journal_file' : forms.FileInput(attrs={'accept' : '.pdf,.zip'})
        }


class EditorialForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.label_suffix = ""


    class Meta:
        model = EditorialModel
        exclude =('application',)

        labels = {
            'editorial_file' : 'Editorial Board',
        }

        widgets = {
            'editorial_file' : forms.FileInput(attrs={'accept' : '.pdf,.zip'})
        }


class AuthorIdsFileForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.label_suffix = ""


    class Meta:
        model = AuthorIdsFileModel
        exclude =('application',)

        labels = {
            'author_ids_file' : 'IDs of the Authors',
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
        exclude =('application',)

        labels = {
            'memorandum_of_appointment_file' : 'Memorandum of Appointment',
        }

        widgets = {
            'memorandum_of_appointment_file' : forms.FileInput(attrs={'accept' : '.pdf,.zip'})
        }
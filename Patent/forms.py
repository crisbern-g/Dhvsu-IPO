from django import forms
from .models import PatentApplicationModel, PatentDraftFileModel, InventionPicturesFileModel, AuthorIdsFileModel, MemorandumOfAppointmentFileModel, AbstractFileModel

class AddPatentForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.label_suffix = ""

    class Meta:
        model = PatentApplicationModel
        exclude = ('patent_slug',)

        labels = {
            'patent_application_name' : 'Name',
            'remarks' : 'Remarks'
        }


class EditRemarksForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.label_suffix = ""

    class Meta:
        model = PatentApplicationModel
        exclude = ('patent_slug', 'patent_application_name')

        labels = {
            'Remarks' : 'Remarks'
        }


class PatentDraftFileForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.label_suffix = ""


    class Meta:
        model = PatentDraftFileModel
        exclude =('patent_application',)

        labels = {
            'patent_draft_file' : 'Patent Draft',
        }

        widgets = {
            'patent_draft_file' : forms.FileInput(attrs={'accept' : '.pdf,.zip'})
        }


class InventionPicturesFileForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.label_suffix = ""


    class Meta:
        model = InventionPicturesFileModel
        exclude =('patent_application',)

        labels = {
            'invention_pictures_file' : 'Pictures of the Invention',
        }

        widgets = {
            'invention_pictures_file' : forms.FileInput(attrs={'accept' : '.pdf,.zip'})
        }


class AbstractFileForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.label_suffix = ""


    class Meta:
        model = AbstractFileModel
        exclude =('patent_application',)

        labels = {
            'abstract_file' : 'Abstract',
        }

        widgets = {
            'abstract_file' : forms.FileInput(attrs={'accept' : '.pdf,.zip'})
        }


class AuthorIdsFileForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.label_suffix = ""


    class Meta:
        model = AuthorIdsFileModel
        exclude =('patent_application',)

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
        exclude =('patent_application',)

        labels = {
            'memorandum_of_appointment_file' : 'Memorandum of Appointment',
        }

        widgets = {
            'memorandum_of_appointment_file' : forms.FileInput(attrs={'accept' : '.pdf,.zip'})
        }
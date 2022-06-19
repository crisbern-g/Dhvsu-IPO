from django import forms
from .models import UtilityModelApplicationModel, DraftFileModel, InventionPicturesFileModel, AbstractFileModel, AuthorIdsFileModel, MemorandumOfAppointmentFileModel

class AddUtilityModelForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.label_suffix = ""

    class Meta:
        model = UtilityModelApplicationModel
        exclude = ('utility_model_slug',)

        labels = {
            'utility_model_application_name' : 'Name',
            'remarks' : 'Remarks'
        }


class EditRemarksForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.label_suffix = ""

    class Meta:
        model = UtilityModelApplicationModel
        exclude = ('utility_model_slug', 'utility_model_application_name')

        labels = {
            'Remarks' : 'Remarks'
        }


class DraftFileForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.label_suffix = ""


    class Meta:
        model = DraftFileModel
        exclude =('utility_model_application',)

        labels = {
            'draft_file' : 'Utility Model Draft',
        }

        widgets = {
            'draft_file' : forms.FileInput(attrs={'accept' : '.pdf,.zip'})
        }


class InventionPicturesFileForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.label_suffix = ""


    class Meta:
        model = InventionPicturesFileModel
        exclude =('utility_model_application',)

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
        exclude =('utility_model_application',)

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
        exclude =('utility_model_application',)

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
        exclude =('utility_model_application',)

        labels = {
            'memorandum_of_appointment_file' : 'Memorandum of Appointment',
        }

        widgets = {
            'memorandum_of_appointment_file' : forms.FileInput(attrs={'accept' : '.pdf,.zip'})
        }
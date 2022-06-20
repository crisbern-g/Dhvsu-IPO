from django import forms
from .models import TrademarkApplicationModel, ApplicationFormModel, MarkFileModel, AuthorIdsFileModel, MemorandumOfAppointmentFileModel

class AddTrademarkApplicationForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.label_suffix = ""

    class Meta:
        model = TrademarkApplicationModel
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
        model = TrademarkApplicationModel
        exclude = ('slug', 'application_name')

        labels = {
            'Remarks' : 'Remarks'
        }


class ApplicationFormForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.label_suffix = ""


    class Meta:
        model = ApplicationFormModel
        exclude =('application',)

        labels = {
            'application_form_file' : 'Application Form',
        }

        widgets = {
            'application_form_file' : forms.FileInput(attrs={'accept' : '.pdf,.zip'})
        }


class MarkFileForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.label_suffix = ""


    class Meta:
        model = MarkFileModel
        exclude =('application',)

        labels = {
            'mark_file' : 'Mark',
        }

        widgets = {
            'mark_file' : forms.FileInput(attrs={'accept' : '.pdf,.zip'})
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
from django.utils.text import slugify
from django.db import models
from django.core.validators import FileExtensionValidator
from django.utils.crypto import get_random_string

def custom_upload_path(instance, filename):
    return f'patent/{instance.utility_model_application.utility_model_application_name}/{filename}'


class UtilityModelApplicationModel(models.Model):
    utility_model_application_name = models.CharField(max_length=200, unique=True)
    date_added = models.DateTimeField(auto_now_add=True, editable=False, null=True)
    date_modified = models.DateTimeField(auto_now=True, null=True)
    remarks = models.TextField(null=True, blank=True)
    utility_model_slug = models.SlugField(null=True, db_index=True, unique=True)

    def save(self, *args, **kwargs):
        if self.utility_model_slug == None:
            self.utility_model_slug = slugify(self.utility_model_application_name)
            self.utility_model_slug = self.utility_model_slug + get_random_string(length=8)

        super().save(*args, **kwargs)


    def __str__(self):
        return self.utility_model_application_name


class DraftFileModel(models.Model):
    patent_draft_file = models.FileField(upload_to=custom_upload_path, validators=[FileExtensionValidator(['pdf', 'zip'])])
    utility_model_application = models.ForeignKey(UtilityModelApplicationModel, related_name='draft_file', on_delete=models.CASCADE, null=True)
    date_added = models.DateTimeField(auto_now_add=True, editable=False)
    date_modified = models.DateTimeField(auto_now=True)


class InventionPicturesFileModel(models.Model):
    invention_pictures_file = models.FileField(upload_to=custom_upload_path, validators=[FileExtensionValidator(['pdf', 'zip'])])
    utility_model_application = models.ForeignKey(UtilityModelApplicationModel, related_name='invention_pictures', on_delete=models.CASCADE, null=True)
    date_added = models.DateTimeField(auto_now_add=True, editable=False)
    date_modified = models.DateTimeField(auto_now=True)


class AbstractFileModel(models.Model):
    abstract_file = models.FileField(upload_to=custom_upload_path, validators=[FileExtensionValidator(['pdf', 'zip'])])
    utility_model_application = models.ForeignKey(UtilityModelApplicationModel, related_name='abstract_file', on_delete=models.CASCADE, null=True)
    date_added = models.DateTimeField(auto_now_add=True, editable=False)
    date_modified = models.DateTimeField(auto_now=True)


class AuthorIdsFileModel(models.Model):
    author_ids_file = models.FileField(upload_to=custom_upload_path, validators=[FileExtensionValidator(['pdf', 'zip'])])
    utility_model_application = models.ForeignKey(UtilityModelApplicationModel, related_name='author_ids', on_delete=models.CASCADE, null=True)
    date_added = models.DateTimeField(auto_now_add=True, editable=False)
    date_modified = models.DateTimeField(auto_now=True)


class MemorandumOfAppointmentFileModel(models.Model):
    memorandum_of_appointment_file = models.FileField(upload_to=custom_upload_path, validators=[FileExtensionValidator(['pdf', 'zip'])])
    utility_model_application = models.ForeignKey(UtilityModelApplicationModel, related_name='memorandum_of_appointment', on_delete=models.CASCADE, null=True)
    date_added = models.DateTimeField(auto_now_add=True, editable=False)
    date_modified = models.DateTimeField(auto_now=True)
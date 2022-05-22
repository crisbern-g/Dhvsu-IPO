from django.utils.text import slugify
from django.db import models
from django.core.validators import FileExtensionValidator
from django.utils.crypto import get_random_string

def custom_upload_path(instance, filename):
    return f'patent/{instance.patent_application.patent_application_name}/{filename}'


class PatentApplicationModel(models.Model):
    patent_application_name = models.CharField(max_length=200, unique=True)
    date_added = models.DateTimeField(auto_now_add=True, editable=False, null=True)
    date_modified = models.DateTimeField(auto_now=True, null=True)
    remarks = models.TextField(null=True, blank=True)
    patent_slug = models.SlugField(null=True, db_index=True, unique=True)

    def save(self, *args, **kwargs):
        if self.patent_slug == None:
            self.patent_slug = slugify(self.patent_application_name)
            self.patent_slug = self.patent_slug + get_random_string(length=8)

        super().save(*args, **kwargs)


    def __str__(self):
        return self.patent_application_name


class PatentDraftFileModel(models.Model):
    patent_draft_file = models.FileField(upload_to=custom_upload_path, validators=[FileExtensionValidator(['pdf', 'zip'])])
    patent_application = models.ForeignKey(PatentApplicationModel, related_name='patent_draft', on_delete=models.CASCADE, null=True)
    date_added = models.DateTimeField(auto_now_add=True, editable=False)
    date_modified = models.DateTimeField(auto_now=True)


class InventionPicturesFileModel(models.Model):
    invention_pictures_file = models.FileField(upload_to=custom_upload_path, validators=[FileExtensionValidator(['pdf', 'zip'])])
    patent_application = models.ForeignKey(PatentApplicationModel, related_name='invention_pictures', on_delete=models.CASCADE, null=True)
    date_added = models.DateTimeField(auto_now_add=True, editable=False)
    date_modified = models.DateTimeField(auto_now=True)


class AbstractFileModel(models.Model):
    abstract_file = models.FileField(upload_to=custom_upload_path, validators=[FileExtensionValidator(['pdf', 'zip'])])
    patent_application = models.ForeignKey(PatentApplicationModel, related_name='abstract_file', on_delete=models.CASCADE, null=True)
    date_added = models.DateTimeField(auto_now_add=True, editable=False)
    date_modified = models.DateTimeField(auto_now=True)


class AuthorIdsFileModel(models.Model):
    author_ids_file = models.FileField(upload_to=custom_upload_path, validators=[FileExtensionValidator(['pdf', 'zip'])])
    patent_application = models.ForeignKey(PatentApplicationModel, related_name='author_ids', on_delete=models.CASCADE, null=True)
    date_added = models.DateTimeField(auto_now_add=True, editable=False)
    date_modified = models.DateTimeField(auto_now=True)


class MemorandumOfAppointmentFileModel(models.Model):
    memorandum_of_appointment_file = models.FileField(upload_to=custom_upload_path, validators=[FileExtensionValidator(['pdf', 'zip'])])
    patent_application = models.ForeignKey(PatentApplicationModel, related_name='memorandum_of_appointment', on_delete=models.CASCADE, null=True)
    date_added = models.DateTimeField(auto_now_add=True, editable=False)
    date_modified = models.DateTimeField(auto_now=True)
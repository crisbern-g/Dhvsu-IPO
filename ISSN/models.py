from django.utils.text import slugify
from django.db import models
from django.core.validators import FileExtensionValidator
from django.utils.crypto import get_random_string

# Create your models here.

def custom_upload_path(instance, filename):
    return f'ISSN/{instance.application.application_name}/{filename}'


class IssnApplicationModel(models.Model):
    application_name = models.CharField(max_length=200, unique=True)
    date_added = models.DateTimeField(auto_now_add=True, editable=False, null=True)
    date_modified = models.DateTimeField(auto_now=True, null=True)
    remarks = models.TextField(null=True, blank=True)
    slug = models.SlugField(null=True, db_index=True, unique=True)

    def save(self, *args, **kwargs):
        if self.slug == None:
            self.slug = slugify(self.application_name)
            self.slug = self.slug + get_random_string(length=8)

        super().save(*args, **kwargs)


    def __str__(self):
        return self.application_name


class JournalModel(models.Model):
    journal_file = models.FileField(upload_to=custom_upload_path, validators=[FileExtensionValidator(['pdf', 'zip'])])
    application = models.ForeignKey(IssnApplicationModel, related_name='journal', on_delete=models.CASCADE, null=True)
    date_added = models.DateTimeField(auto_now_add=True, editable=False)
    date_modified = models.DateTimeField(auto_now=True)


class EditorialModel(models.Model):
    editorial_file = models.FileField(upload_to=custom_upload_path, validators=[FileExtensionValidator(['pdf', 'zip'])])
    application = models.ForeignKey(IssnApplicationModel, related_name='editorial', on_delete=models.CASCADE, null=True)
    date_added = models.DateTimeField(auto_now_add=True, editable=False)
    date_modified = models.DateTimeField(auto_now=True)


class AuthorIdsFileModel(models.Model):
    author_ids_file = models.FileField(upload_to=custom_upload_path, validators=[FileExtensionValidator(['pdf', 'zip'])])
    application = models.ForeignKey(IssnApplicationModel, related_name='author_ids', on_delete=models.CASCADE, null=True)
    date_added = models.DateTimeField(auto_now_add=True, editable=False)
    date_modified = models.DateTimeField(auto_now=True)


class MemorandumOfAppointmentFileModel(models.Model):
    memorandum_of_appointment_file = models.FileField(upload_to=custom_upload_path, validators=[FileExtensionValidator(['pdf', 'zip'])])
    application = models.ForeignKey(IssnApplicationModel, related_name='memorandum_of_appointment', on_delete=models.CASCADE, null=True)
    date_added = models.DateTimeField(auto_now_add=True, editable=False)
    date_modified = models.DateTimeField(auto_now=True)
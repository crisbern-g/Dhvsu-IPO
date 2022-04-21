from django.utils.text import slugify
from django.db import models
from django.core.validators import FileExtensionValidator

def custom_upload_path(instance, filename):
    return f'copyright/{instance.copyright_application.copyright_application_name}/{filename}'


class CopyRightApplicationModel(models.Model):
    copyright_application_name = models.CharField(max_length=200, unique=True)
    date_added = models.DateTimeField(auto_now_add=True, editable=False, null=True)
    date_modified = models.DateTimeField(auto_now=True, null=True)
    remarks = models.TextField(null=True, blank=True)
    copyright_slug = models.SlugField(null=True, db_index=True)


    def save(self, *args, **kwargs):
        self.copyright_slug = slugify(self.copyright_application_name)

        super().save(*args, **kwargs)

    def __str__(self):
        return self.copyright_application_name


class CopyrightApplicationFileModel(models.Model):
    application_file = models.FileField(upload_to=custom_upload_path, validators=[FileExtensionValidator(['pdf', 'zip'])])
    copyright_application = models.ForeignKey(CopyRightApplicationModel, related_name='copyright_application', on_delete=models.CASCADE)
    date_added = models.DateTimeField(auto_now_add=True, editable=False)
    date_modified = models.DateTimeField(auto_now=True)


class DeedOfAssignmentFileModel(models.Model):
    deed_of_assignment_file = models.FileField(upload_to=custom_upload_path, validators=[FileExtensionValidator(['pdf', 'zip'])])
    copyright_application = models.ForeignKey(CopyRightApplicationModel, related_name='deed_of_assignment', on_delete=models.CASCADE)
    date_added = models.DateTimeField(auto_now_add=True, editable=False)
    date_modified = models.DateTimeField(auto_now=True)


class ElectronicCopyFileModel(models.Model):
    electronic_copy_file = models.FileField(upload_to=custom_upload_path, validators=[FileExtensionValidator(['pdf', 'zip'])])
    copyright_application = models.ForeignKey(CopyRightApplicationModel, related_name='electronic_copy', on_delete=models.CASCADE)
    date_added = models.DateTimeField(auto_now_add=True, editable=False)
    date_modified = models.DateTimeField(auto_now=True)
    

class AuthorIdsFileModel(models.Model):
    author_ids_file = models.FileField(upload_to=custom_upload_path, validators=[FileExtensionValidator(['pdf', 'zip'])])
    copyright_application = models.ForeignKey(CopyRightApplicationModel, related_name='author_ids', on_delete=models.CASCADE)
    date_added = models.DateTimeField(auto_now_add=True, editable=False)
    date_modified = models.DateTimeField(auto_now=True)


class MemorandumOfAppointmentFileModel(models.Model):
    memorandum_of_appointment_file = models.FileField(upload_to=custom_upload_path, validators=[FileExtensionValidator(['pdf', 'zip'])])
    copyright_application = models.ForeignKey(CopyRightApplicationModel, related_name='memorandum_of_appointment', on_delete=models.CASCADE)
    date_added = models.DateTimeField(auto_now_add=True, editable=False)
    date_modified = models.DateTimeField(auto_now=True)


class CertificateOfRegistrationFileModel(models.Model):
    certificate_of_registration_file = models.FileField(upload_to=custom_upload_path, validators=[FileExtensionValidator(['pdf', 'zip'])])
    copyright_application = models.ForeignKey(CopyRightApplicationModel, related_name='certificate_of_registration', on_delete=models.CASCADE)
    date_added = models.DateTimeField(auto_now_add=True, editable=False)
    date_modified = models.DateTimeField(auto_now=True)
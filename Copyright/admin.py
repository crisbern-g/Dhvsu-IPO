from django.contrib import admin
from .models import CopyRightApplicationModel, CopyrightApplicationFileModel, DeedOfAssignmentFileModel, ElectronicCopyFileModel, AuthorIdsFileModel, MemorandumOfAppointmentFileModel, CertificateOfRegistrationFileModel

# Register your models here.
admin.site.register(CopyRightApplicationModel)
admin.site.register(CopyrightApplicationFileModel)
admin.site.register(DeedOfAssignmentFileModel)
admin.site.register(ElectronicCopyFileModel)
admin.site.register(AuthorIdsFileModel)
admin.site.register(MemorandumOfAppointmentFileModel)
admin.site.register(CertificateOfRegistrationFileModel)
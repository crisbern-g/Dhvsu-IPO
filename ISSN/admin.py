from django.contrib import admin
from . import models

# Register your models here.
admin.site.register(models.IssnApplicationModel)
admin.site.register(models.JournalModel)
admin.site.register(models.EditorialModel)
admin.site.register(models.AuthorIdsFileModel)
admin.site.register(models.MemorandumOfAppointmentFileModel)
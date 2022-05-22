from django.contrib import admin
from . import models

# Register your models here.
admin.site.register(models.UtilityModelApplicationModel)
admin.site.register(models.DraftFileModel)
admin.site.register(models.InventionPicturesFileModel)
admin.site.register(models.AbstractFileModel)
admin.site.register(models.AuthorIdsFileModel)
admin.site.register(models.MemorandumOfAppointmentFileModel)
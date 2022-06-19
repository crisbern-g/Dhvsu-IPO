from django.contrib import admin
from . import models

# Register your models here.
admin.site.register(models.TrademarkApplicationModel)
admin.site.register(models.ApplicationFormModel)
admin.site.register(models.MarkFileModel)
admin.site.register(models.AuthorIdsFileModel)
admin.site.register(models.MemorandumOfAppointmentFileModel)
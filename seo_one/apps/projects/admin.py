from django.contrib import admin
from . import models

# Register your models here.

admin.site.register(models.User)
admin.site.register(models.Project)
admin.site.register(models.Admin_panel)
admin.site.register(models.Server)
admin.site.register(models.Yandex_account)
admin.site.register(models.Google_account)
admin.site.register(models.Standart_task)
admin.site.register(models.Task)
admin.site.register(models.Reqest)
admin.site.register(models.Page_url)
admin.site.register(models.Result)
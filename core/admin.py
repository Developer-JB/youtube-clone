from django.contrib import admin
from . models import Video
from import_export.admin import ImportExportModelAdmin
# Register your models here.
class VideoAdmin(ImportExportModelAdmin):
    pass

admin.site.register(Video,VideoAdmin)

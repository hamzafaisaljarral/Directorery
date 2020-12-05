#from django.contrib import admin
#from .models import Teachers
# Register your models here.
#admin.site.register(Teachers)

from import_export.admin import ImportExportModelAdmin
from django.contrib import admin
from .models import Teachers


@admin.register(Teachers)
class PersonAdmin(ImportExportModelAdmin):
    pass
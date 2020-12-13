#from django.contrib import admin
#from .models import Teachers
# Register your models here.
#admin.site.register(Teachers)

from import_export.admin import ImportExportModelAdmin
from django.contrib import admin
from .models import Teachers
from import_export import resources
from django.core.exceptions import ValidationError
from import_export.fields import Field
from import_export.admin import ImportExportModelAdmin
import json

#@admin.register(Teachers)
#class PersonAdmin(ImportExportModelAdmin):
#    pass

class TeacherResource(resources.ModelResource):
    First_Name = Field(attribute='First_Name', column_name='First Name')
    Last_Name = Field(attribute='Last_Name', column_name='Last Name')
    Profile_picture = Field(attribute='Profile_picture', column_name='Profile picture')
    Email_Address = Field(attribute='Email_Address', column_name='Email Address')
    Phone_Number = Field(attribute='Phone_Number', column_name='Phone Number')
    Room_Number = Field(attribute='Room_Number', column_name='Room Number')
    Subjects_taught = Field(attribute='Subjects_taught', column_name='Subjects taught')
    

    def get_import_headers(self):
        headers = super().get_import_headers()
        for i, h in enumerate(headers):
            if h == 'First Name':
                headers[i] = 'First_Name'
            if h == 'Last Name':
                headers[i] = 'Last_Name'
            if h == 'Profile picture':
                headers[i] = 'Profile_picture'
            if h == 'Email Address':
                headers[i] = 'Email_Address'
            if h == 'Phone Number':
                headers[i] = 'Phone_Number'
            if h == 'Room Number':
                headers[i] = 'Room_Number'
            if h == 'Subjects taught':
                headers[i] = 'Subjects_taught'
            
    def before_save_instance(self, instance, using_transactions, dry_run):
        sub=instance.Subjects_taught
        if (len(sub.split(',')) > 5):
            raise ValidationError('you can add 5 or less than 5 subjects')            
        return instance

    class Meta:
        model = Teachers
        import_id_fields = ('First_Name',)
        export_order = ('First_Name', 'Last_Name', 'Profile_picture', 'Email_Address', 'Phone_Number', 'Room_Number',
                        'Subjects_taught')

        skip_unchanged = True
        report_skipped = False
    
    

class TeacherAdmin(ImportExportModelAdmin):
    resource_class =TeacherResource

admin.site.register(Teachers, TeacherAdmin)    
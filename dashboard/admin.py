from django.contrib import admin
from .models import IndustrialData
from import_export import resources
from import_export.admin import ImportExportModelAdmin

# Register your models here.
class IndustrialResource(resources.ModelResource):
    class Meta:
        model=IndustrialData

class IndustrialAdmin(ImportExportModelAdmin):
    resource_class = IndustrialResource

admin.site.register(IndustrialData,IndustrialAdmin)
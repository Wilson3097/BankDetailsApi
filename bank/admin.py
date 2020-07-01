from django.contrib import admin
from .models import *
from import_export.admin import ImportExportModelAdmin
from import_export import resources
# Register your models here.


class BankResource(resources.ModelResource):
    class Meta:
        model = BankDetails
        exclude = ('id',)
        import_id_fields = ('Id',)


class BankAdmin(ImportExportModelAdmin):
    resource_class = BankResource


admin.site.register(BankDetails, BankAdmin)

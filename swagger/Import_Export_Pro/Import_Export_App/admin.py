

from django.contrib import admin
from .models import Person

# class PersonAdmin(admin.ModelAdmin):
#     list_display = ['pname','email','location']
# admin.site.register(Person , PersonAdmin)



from import_export.admin import ImportExportModelAdmin

@admin.register(Person)
class PersonAdmin2(ImportExportModelAdmin):
    pass
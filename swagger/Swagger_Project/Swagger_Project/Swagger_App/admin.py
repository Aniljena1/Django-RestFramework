
#username = Srinivas & pwd = admin123

from django.contrib import admin
from Swagger_App.models import Employee

# Register your models here.
class EmployeeAdmin(admin.ModelAdmin):
    list_display = ['eno','ename' , 'esal','eaddr']

admin.site.register(Employee , EmployeeAdmin)
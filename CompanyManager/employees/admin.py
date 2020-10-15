from django.contrib import admin
from .models import Employee

# Used to customize Django Admin
class EmpAdmin(admin.ModelAdmin):
    readonly_fields = ('dateCreated',)

admin.site.register(Employee, EmpAdmin)

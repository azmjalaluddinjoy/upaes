from django.contrib import admin
from .models import Administration


class AdministrationAdmin(admin.ModelAdmin):
    list_display = ('emp_id', 'full_name', 'designation', 'web_page', 'email', 'password')
# Register your models here.


admin.site.register(Administration, AdministrationAdmin)



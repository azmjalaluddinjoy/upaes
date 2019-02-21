from django.contrib import admin
from information.models import Divisions, Districts


class DistrictAdmin(admin.ModelAdmin):
    list_display = ('name', 'division', 'visited', 'population_density')


class DivisionsAdmin(admin.ModelAdmin):
    list_display = ('name', 'population', 'area')


admin.site.register(Divisions, DivisionsAdmin)
admin.site.register(Districts, DistrictAdmin)







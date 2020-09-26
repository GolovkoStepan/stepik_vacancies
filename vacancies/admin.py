from django.contrib import admin

from vacancies.models import Specialty


class SpecialtyAdmin(admin.ModelAdmin):
    pass


admin.site.register(Specialty, SpecialtyAdmin)

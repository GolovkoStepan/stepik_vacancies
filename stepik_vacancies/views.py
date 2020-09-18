from django.shortcuts import render
from django.views import View
from companies.models import Company
from vacancies.models import Specialty


class MainView(View):
    def get(self, request, *args, **kwargs):
        context = {
            "specialties": Specialty.objects.all(),
            "companies": Company.objects.all(),
        }

        return render(request, 'stepik_vacancies/index.html', context=context)

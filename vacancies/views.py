from django.db.models import Q
from django.shortcuts import render, get_object_or_404
from django.views import View

from vacancies.models import Specialty, Vacancy


class IndexView(View):
    def get(self, request, specialty="all", *args, **kwargs):
        if specialty == "all":
            title = "Все вакансии"
            vacancies = Vacancy.objects.all()
        else:
            spec = get_object_or_404(Specialty, code=specialty)
            title = spec.name
            vacancies = Vacancy.objects.filter(specialty__code=specialty)

        context = {
            "title": title,
            "vacancies": vacancies
        }

        return render(request, 'vacancies/index.html', context=context)


class VacancyView(View):
    def get(self, request, vacancy_id, *args, **kwargs):
        vacancy = get_object_or_404(Vacancy, id=vacancy_id)

        context = {
            "vacancy": vacancy
        }

        return render(request, 'vacancies/vacancy.html', context=context)


class SearchView(View):
    def get(self, request, *args, **kwargs):
        q = request.GET.get('q') or ''
        vacancies = Vacancy.objects.filter(Q(title__contains=q) | Q(description__contains=q))

        context = {
            "vacancies": vacancies,
            'q': q
        }

        return render(request, 'vacancies/search.html', context=context)

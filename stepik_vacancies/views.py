from django.contrib import messages
from django.shortcuts import render, redirect
from django.views import View

from companies.models import Company
from vacancies.models import Specialty


def view_404(request, *args, **kwargs):
    messages.add_message(request, messages.INFO, 'Запрашиваемая вами страница не была найдена')
    return redirect('/')


def view_500(request, *args, **kwargs):
    messages.add_message(request, messages.INFO, 'При обработке вашего запроса произошла ошибка')
    return redirect('/')


class MainView(View):
    def get(self, request, *args, **kwargs):
        context = {
            "specialties": Specialty.objects.all(),
            "companies": Company.objects.all(),
        }

        return render(request, 'stepik_vacancies/index.html', context=context)

from django.urls import path
from vacancies.views import IndexView, VacancyView

urlpatterns = [
    path('', IndexView.as_view()),
    path('<int:vacancy_id>', VacancyView.as_view()),
    path('specialty/<str:specialty>', IndexView.as_view()),
]

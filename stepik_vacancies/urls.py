from django.contrib import admin
from django.urls import path, include

from stepik_vacancies.views import MainView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', MainView.as_view()),
    path('vacancies/', include('vacancies.urls')),
    path('companies/', include('companies.urls'))
]

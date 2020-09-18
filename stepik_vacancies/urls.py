from django.contrib import admin
from django.urls import path, include

from stepik_vacancies.views import MainView, view_404, view_500

handler404 = view_404
handler500 = view_500

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', MainView.as_view()),
    path('vacancies/', include('vacancies.urls')),
    path('companies/', include('companies.urls'))
]

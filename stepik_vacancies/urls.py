from django.contrib import admin
from django.contrib.auth.views import LogoutView
from django.urls import path, include

from stepik_vacancies.views import MainView, view_404, view_500, UserSignupView, UserLoginView, UserResume, \
    UserProfileView
from vacancies.views import SearchView

handler404 = view_404
handler500 = view_500

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', MainView.as_view()),
    path('vacancies/', include('vacancies.urls')),
    path('companies/', include('companies.urls')),
    path('login', UserLoginView.as_view()),
    path('logout', LogoutView.as_view()),
    path('signup', UserSignupView.as_view()),
    path('profile', UserProfileView.as_view()),
    path('my_resume', UserResume.as_view()),
    path('search', SearchView.as_view())
]

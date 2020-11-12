from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView
from django.contrib.messages.views import SuccessMessageMixin
from django.shortcuts import render, redirect
from django.views import View
from django.views.generic import CreateView, UpdateView

from companies.models import Company
from stepik_vacancies.forms import CreateUserForm, LoginUserForm, UserProfileForm
from vacancies.forms import UserResumeForm
from vacancies.models import Specialty, Resume


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


class UserSignupView(SuccessMessageMixin, CreateView):
    form_class = CreateUserForm
    success_url = 'login'
    template_name = 'stepik_vacancies/signup.html'
    success_message = 'Вы успешно зарегестрировались!'


class UserLoginView(SuccessMessageMixin, LoginView):
    form_class = LoginUserForm
    redirect_authenticated_user = True
    template_name = 'stepik_vacancies/login.html'
    success_message = 'Добро пожаловать!'


class UserProfileView(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    form_class = UserProfileForm
    success_url = 'profile'
    template_name = 'stepik_vacancies/profile.html'
    success_message = 'Ваш профиль успешно изменен'

    def get_object(self, queryset=None):
        return self.request.user

    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            messages.add_message(request, messages.INFO, 'Чтобы изменить профиль, необходимо войти')
            return redirect('/login')
        return super().dispatch(request, *args, **kwargs)


class UserResume(LoginRequiredMixin, View):
    def get(self, request, *args, **kwargs):
        if request.GET.get('create'):
            request.user.resume = Resume()
            form = UserResumeForm()
        else:
            if request.user.has_resume():
                form = UserResumeForm(instance=request.user.resume)
            else:
                form = UserResumeForm()

        return render(request, 'stepik_vacancies/resume.html', context={"form": form})

    def post(self, request, *args, **kwargs):
        if request.user.has_resume():
            form = UserResumeForm(request.POST, instance=request.user.resume)

            if form.is_valid():
                form.save()
                messages.add_message(request, messages.INFO, 'Ваше резюме обновлено!')
        else:
            form = UserResumeForm(request.POST)

            if form.is_valid():
                resume = form.save(commit=False)
                resume.user = request.user
                resume.save()
                messages.add_message(request, messages.INFO, 'Ваше резюме создано!')

        return redirect('/my_resume')

    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            messages.add_message(request, messages.INFO, 'Чтобы изменить или создать резюме, необходимо войти')
            return redirect('/login')
        return super().dispatch(request, *args, **kwargs)

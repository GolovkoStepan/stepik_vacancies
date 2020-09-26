from django.contrib.auth.models import User
from django.db import models
from django.utils.translation import gettext_lazy as _

from companies.models import Company


class Specialty(models.Model):
    code = models.CharField(max_length=100)
    name = models.CharField(max_length=200)
    image = models.CharField(max_length=250)

    def __str__(self):
        return self.name


class Vacancy(models.Model):
    title = models.CharField(max_length=250)
    specialty = models.ForeignKey(Specialty, on_delete=models.CASCADE, related_name="vacancies")
    company = models.ForeignKey(Company, on_delete=models.CASCADE, related_name="vacancies")
    skills = models.CharField(max_length=350)
    description = models.TextField()
    salary_min = models.FloatField()
    salary_max = models.FloatField()
    published_at = models.DateTimeField()


class Resume(models.Model):
    class WorkStatuses(models.TextChoices):
        NOT_LOOKING = 'NL', _('Не ищю работу')
        READY_TO_OFFERS = 'RTO', _('Готов к предложениям')
        LOOKING_JOB = 'LJ', _('Ищу работу')

    class Qualifications(models.TextChoices):
        INTERN = 'INTERN', _('Стажер')
        JUNIOR = 'JUNIOR', _('Младший разработчик')
        MIDDLE = 'MIDDLE', _('Разработчик')
        SENIOR = 'SENIOR', _('Старший разработчик')
        LEAD = 'LEAD', _('Руководитель разработки')

    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='resume')
    status = models.CharField(max_length=10, choices=WorkStatuses.choices, default=WorkStatuses.LOOKING_JOB)
    salary = models.FloatField()
    specialty = models.ForeignKey(Specialty, on_delete=models.CASCADE)
    grade = models.CharField(max_length=50, choices=Qualifications.choices, default=Qualifications.JUNIOR)
    education = models.TextField(max_length=500)
    experience = models.TextField(max_length=500)
    portfolio = models.CharField(max_length=100)


def get_user_name(self):
    if self.first_name or self.last_name:
        return self.first_name + " " + self.last_name
    return self.username


def has_resume(self):
    try:
        _var = self.resume
        return True
    except User.resume.RelatedObjectDoesNotExist:
        return False


User.add_to_class("get_user_name", get_user_name)
User.add_to_class("has_resume", has_resume)

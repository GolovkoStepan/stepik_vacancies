from django.db import models
from companies.models import Company


class Specialty(models.Model):
    code = models.CharField(max_length=100)
    name = models.CharField(max_length=200)
    image = models.CharField(max_length=250)


class Vacancy(models.Model):
    title = models.CharField(max_length=250)
    specialty = models.ForeignKey(Specialty, on_delete=models.CASCADE, related_name="vacancies")
    company = models.ForeignKey(Company, on_delete=models.CASCADE, related_name="vacancies")
    skills = models.CharField(max_length=350)
    description = models.TextField()
    salary_min = models.FloatField()
    salary_max = models.FloatField()
    published_at = models.DateTimeField()

from django.db import models


class Company(models.Model):
    name = models.CharField(max_length=250)
    location = models.CharField(max_length=100)
    logo = models.CharField(max_length=250)
    description = models.TextField()
    employee_count = models.IntegerField()

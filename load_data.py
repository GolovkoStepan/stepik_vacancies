import os
import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", 'stepik_vacancies.settings')
django.setup()

import random
from datetime import datetime
from companies.models import Company
from vacancies.models import Specialty, Vacancy

if __name__ == '__main__':
    """Delete all before add data"""
    Company.objects.all().delete()
    Specialty.objects.all().delete()
    Vacancy.objects.all().delete()

    """Load companies"""
    workiro = Company.objects.create(
        name="workiro",
        logo="https://place-hold.it/100x60",
        location="Москва",
        description="Потом добавим",
        employee_count=random.randint(15, 150)
    )
    rebelrage = Company.objects.create(
        name="rebelrage",
        logo="https://place-hold.it/100x60",
        location="Москва",
        description="Потом добавим",
        employee_count=random.randint(15, 150)
    )
    staffingsmarter = Company.objects.create(
        name="staffingsmarter",
        logo="https://place-hold.it/100x60",
        location="Москва",
        description="Потом добавим",
        employee_count=random.randint(15, 150)
    )
    evilthreath = Company.objects.create(
        name="evilthreath",
        logo="https://place-hold.it/100x60",
        location="Москва",
        description="Потом добавим",
        employee_count=random.randint(15, 150)
    )
    hirey = Company.objects.create(
        name="hirey",
        logo="https://place-hold.it/100x60",
        location="Москва",
        description="Потом добавим",
        employee_count=random.randint(15, 150)
    )
    swiftattack = Company.objects.create(
        name="swiftattack",
        logo="https://place-hold.it/100x60",
        location="Москва",
        description="Потом добавим",
        employee_count=random.randint(15, 150)
    )
    troller = Company.objects.create(
        name="troller",
        logo="https://place-hold.it/100x60",
        location="Москва",
        description="Потом добавим",
        employee_count=random.randint(15, 150)
    )
    primalassault = Company.objects.create(
        name="primalassault",
        logo="https://place-hold.it/100x60",
        location="Москва",
        description="Потом добавим",
        employee_count=random.randint(15, 150)
    )

    """Load specialties"""
    frontend = Specialty.objects.create(
        code="frontend",
        name="Фронтенд",
        image="https://place-hold.it/100x60"
    )
    backend = Specialty.objects.create(
        code="backend",
        name="Бэкенд",
        image="https://place-hold.it/100x60"
    )
    gamedev = Specialty.objects.create(
        code="gamedev",
        name="Геймдев",
        image="https://place-hold.it/100x60"
    )
    devops = Specialty.objects.create(
        code="devops",
        name="Девопс",
        image="https://place-hold.it/100x60"
    )
    design = Specialty.objects.create(
        code="design",
        name="Дизайн",
        image="https://place-hold.it/100x60"
    )
    products = Specialty.objects.create(
        code="products",
        name="Продукты",
        image="https://place-hold.it/100x60"
    )
    management = Specialty.objects.create(
        code="management",
        name="Менеджмент",
        image="https://place-hold.it/100x60"
    )
    testing = Specialty.objects.create(
        code="testing",
        name="Тестирование",
        image="https://place-hold.it/100x60"
    )

    """Load vacancies"""
    vacancy_1 = Vacancy.objects.create(
        title="Разработчик на Python",
        specialty=backend,
        skills="Python Django",
        company=staffingsmarter,
        salary_min=100000,
        salary_max=150000,
        published_at=datetime.today(),
        description="Потом добавим"
    )
    vacancy_2 = Vacancy.objects.create(
        title="Разработчик в проект на Django",
        specialty=backend,
        skills="Python Django",
        company=swiftattack,
        salary_min=80000,
        salary_max=90000,
        published_at=datetime.today(),
        description="Потом добавим"
    )
    vacancy_3 = Vacancy.objects.create(
        title="Разработчик на Swift в аутсорс компанию",
        specialty=backend,
        skills="Swift",
        company=swiftattack,
        salary_min=120000,
        salary_max=150000,
        published_at=datetime.today(),
        description="Потом добавим"
    )
    vacancy_4 = Vacancy.objects.create(
        title="Мидл программист на Python",
        specialty=backend,
        skills="Python Django",
        company=workiro,
        salary_min=80000,
        salary_max=90000,
        published_at=datetime.today(),
        description="Потом добавим"
    )
    vacancy_5 = Vacancy.objects.create(
        title="Питонист в стартап",
        specialty=backend,
        skills="Python Django",
        company=primalassault,
        salary_min=120000,
        salary_max=150000,
        published_at=datetime.today(),
        description="Потом добавим"
    )

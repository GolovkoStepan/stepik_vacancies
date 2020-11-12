from django.shortcuts import render, get_object_or_404
from django.views import View

from companies.models import Company


class CompanyView(View):
    def get(self, request, company_id, *args, **kwargs):
        company = get_object_or_404(Company, id=company_id)

        context = {
            "company": company
        }

        return render(request, 'companies/company.html', context=context)

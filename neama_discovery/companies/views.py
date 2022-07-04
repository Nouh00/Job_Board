from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse, reverse_lazy
from .models import Company
from opportunities.models import Opportunity
from django.db.models import Q
from .forms import createCompanyForm
from django.contrib.auth.models import User


def companies(request):
    q = request.GET.get('q') if request.GET.get('q') != None else ""
    companies = Company.objects.filter(
        Q(name__icontains=q) |
        Q(description__icontains=q) |
        Q(location__icontains=q)
    )

    context = {
        "companies": companies
    }

    return render(request, 'base/companies_list.html', context)


def singlCompany(request, pk):
    company = Company.objects.get(id=pk)
    company_opport = Opportunity.objects.filter(company=company)

    context = {
        "company":Company,
        "company_opportunity": company_opport
    }
    return render(request, 'base/company_single.html', context)


def addCompany(request):
    form = createCompanyForm
    user = get_object_or_404(User, id=request.user.id)
    company = Company.objects.filter(user=user)

    if not company:
        if request.method == 'POST':
            form = form(request.POST)
            if form.is_valid:
                instance = form.save(commit=False)
                instance.user = user
                instance.save()
                return redirect(reverse('single-company', kwargs={"pk": instance.id}))
                

    context ={"form":form}
    return render(request, 'base/pages/company/create_company.html', context)



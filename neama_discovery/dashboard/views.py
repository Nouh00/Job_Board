from django.shortcuts import render, redirect, get_object_or_404
from opportunities.forms import OpportunityForm
from django.contrib.auth.models import User
from django.urls import reverse, reverse_lazy
from opportunities.models import Opportunity
from django.db.models import Q


# Create your views here.

def companyDashboard(request):
    return render(request, "base/pages/company/dashboard.html")

def companyOpportunities(request):
    user = get_object_or_404(User, id=request.user.id)
    q = request.GET.get('q') if request.GET.get('q') != None else ""
    opportunities = Opportunity.objects.filter(user__id=user.id)
    company_opportunities = opportunities.filter(
        Q(title__icontains=q) |
        Q(description__icontains=q) |
        Q(location__icontains=q) |
        Q(opportunity_type__icontains=q)
    )
    context = {
        "opportunities": company_opportunities
    }
    return render(request, "base/pages/company/my_opportunities.html", context)

def createOpportunity(request):
    form = OpportunityForm
    user = get_object_or_404(User, id=request.user.id)

    if request.method == 'POST':
        form = form(request.POST)
        if form.is_valid:
            instance = form.save(commit=False)
            instance.user = user
            instance.save()
            form.save_m2m()
            redirect(reverse('single-opportunity', kwargs={"pk": instance.id}))

    context ={"form":form}
    return render(request, "base/pages/company/add_opportunity.html", context)
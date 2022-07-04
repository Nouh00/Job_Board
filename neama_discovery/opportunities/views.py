from multiprocessing import context
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from .models import Applicant, Opportunity
from .forms import OpportunityForm,OpportunityApplyForm
from companies.models import Company
from django.db.models import Q
from django.urls import reverse, reverse_lazy
from django.contrib.auth.models import User
from django.contrib import messages





def opportunities(request):
    q = request.GET.get('q') if request.GET.get('q') != None else ""
    opportunities = Opportunity.objects.filter(
        Q(title__icontains=q) |
        Q(description__icontains=q) |
        Q(location__icontains=q) |
        Q(opportunity_type__icontains=q)
    )

    context = {
        "opportunities": opportunities
    }

    return render(request, 'base/opportunities_list.html', context)



def singlOpportunity(request, pk):
    opportunity = Opportunity.objects.get(id=pk)
    applicants = opportunity.applicants.all()


    context = {
        "opportunity":opportunity,
        "applicants": applicants
    }
    return render(request, 'base/opportunity_single.html', context)

def addOpportunity(request):
    form = OpportunityForm
    user = get_object_or_404(User, id=request.user.id)

    if request.method == 'POST':
        form = form(request.POST)
        if form.is_valid:
            instance = form.save(commit=False)
            instance.user = user
            instance.save()
            return redirect(reverse('single-opportunity', kwargs={"pk": instance.id}))


    context={"form":form}
    return render(request, 'base/add_opportunity_form.html', context) 

def applyOpportunity(request, pk):
    form = OpportunityApplyForm(request.POST)

    user = get_object_or_404(User, id=request.user.id)
    applicant = Applicant.objects.filter(user=user, opportunity=pk)

    if not applicant:
        if request.method == "POST":
            if form.is_valid():
                instance = form.save(commit=False)
                instance.user = user
                instance.save()
                return redirect(reverse('single-opportunity', kwargs={"pk": instance.id}))
            else:
                return redirect(reverse('single-opportunity', kwargs={"pk": instance.id}))
        else:
            return redirect(reverse('single-opportunity', kwargs={"pk": instance.id}))
    
    else:
        return redirect(reverse('single-opportunity', kwargs={"pk": instance.id}))
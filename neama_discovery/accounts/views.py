from django.shortcuts import render,redirect, get_object_or_404
from django.http import HttpResponse
from django.urls import reverse, reverse_lazy
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from opportunities.models import Opportunity
from django.contrib.auth.models import User
from .forms import recruiterForm, candidateForm
from .models import Recruiter, candidate


def index(request):
    opportunities = Opportunity.objects.all()[0:3]

    context = {
        "opportunities": opportunities,
        
    }
    return render(request, 'pages/home.html', context)


def loginPage(request):
    page = 'login'

    if request.user.is_authenticated:
        return redirect('home')

    if request.method == 'POST':
        username = request.POST.get("username")
        password = request.POST.get("password")
    
        try:
            user = User.objects.get(username=username)
        except:
            messages.error(request, 'Please Register First because you are not one of us yet 😛!')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, 'Email Or Password does not exist 😛!')

    context = {'page':page}
    return render(request, 'base/login_register.html', context)

def logoutUser(request):
    logout(request)
    return redirect('home')

def recruiterProfile(request, pk):
    user = get_object_or_404(Recruiter, user__id=pk)
    context = {
        "user_data" : user,
    }
    return render(request, 'base/profile/user_profile.html', context)


def updateRecruiter(request,pk):
    user = request.user
    recruiter = Recruiter.objects.get(user=user)
    profile_form = recruiterForm(request.POST or None, instance=recruiter)

    if profile_form.is_valid():
        instance = profile_form.save(commit=False)
        instance.save()
        return redirect('recruiter-profile', pk=user.id)

    context = {
        "profile_form" : profile_form,
        'user':recruiter
    }
    return render(request, 'base/profile/update-profile.html', context)








'''
def registerPage(request):
    page = 'register'
    form = MyUserCreationForm()
    if request.method == 'POST':
        form = MyUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.name = user.name.lower()
            user.save()
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, 'Error Occured Babe 😛!')
    
    context = {'form':form, 'page': page}
    return render(request, 'base/login_register.html', context)

def loginPage(request):
    page = 'login'

    if request.user.is_authenticated:
        return redirect('home')

    if request.method == 'POST':
        email = request.POST.get("email")
        password = request.POST.get("password")
    
        try:
            user = User.objects.get(email=email)
        except:
            messages.error(request, 'Please Register First because you are not one of us yet 😛!')

        user = authenticate(request, email=email, password=password)

        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, 'Email Or Password does not exist 😛!')

    context = {'page':page}
    return render(request, 'base/login_register.html', context)

def logoutUser(request):
    logout(request)
    return redirect('home')

def volProfile(request, pk):
    user = User.objects.get(id=pk)
    context={
        'user':user
        }
    return render(request, 'base/profile/vol_profile.html',context)

@login_required(login_url='/login')
def updateProfileVol(request):
    user = request.user
    form = UserForm(instance=user)
    if request.method == 'POST':
        form = UserForm(request.POST or None, instance=user)
        if form.is_valid():
            print("yes its valid")
            form.save()
            return redirect('base/profile/vol_profile.html', pk=user.id)

    context={"form":form}
    return render(request, 'base/profile/update-volprofile.html', context)
    '''
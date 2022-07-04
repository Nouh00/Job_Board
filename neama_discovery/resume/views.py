from multiprocessing import context
from django.shortcuts import render, get_object_or_404, redirect
from django.forms.models import modelformset_factory
from django.http import HttpResponse, Http404
from .models import Resume, Education, Experience, Work, Publications, Urls
from .forms import resumeForm, educationForm, experienceForm, workForm, publicationsForm, urlsForm, ExperienceFormSet
from accounts.models import Recruiter
from django.urls import reverse





def resume(request, pk):
    resume = Resume.objects.filter(user__id=pk)
    recruiter = Recruiter.objects.get(user=request.user)
    if not resume:
        return redirect('create-resume')

    resume = Resume.objects.get(user__id=pk)
    experiences = Experience.objects.filter(resume__id = resume.id)
    publications = Publications.objects.filter(resume__id = resume.id)
    work = Work.objects.filter(resume__id = resume.id)
    urls = Urls.objects.filter(resume__id = resume.id)
    education = Education.objects.filter(resume__id = resume.id)
    skills = resume.skills
    

    context = {
        'resume':resume,
        "experiences": experiences,
        "publications":publications,
        "work":work,
        "urls":urls,
        "education":education,
        "skills":skills,
        "certificates":"",
        "user":recruiter
    }
    return render(request, 'base/resume.html', context)


def createResume(request):
    user = request.user
    recruiter = Recruiter.objects.get(user=user)
    resume = Resume.objects.get_or_create(user=user)[0]
    Resumeform = resumeForm(instance = resume)
    ExperienceFormset = modelformset_factory(Experience, form=experienceForm, extra=0)
    ExperienceFormset = ExperienceFormset(request.POST or None)
    #qs = recruiter.education_set.all()
    context = {
        "resume_form":Resumeform,
        "experiencesForm":ExperienceFormset,
        "user_data":recruiter,
    }
    print(request.POST)
    if Resumeform.is_valid():
        parent = Resumeform.save(commit=False)
        parent.save()
        context['message'] = 'formset error'
    
    if ExperienceFormset.is_valid():
        for form in ExperienceFormset:
            child = form.save(commit=False)
            child.resume = resume
            child.save()
            context['message'] = 'Data Saved'

    
    return render(request, 'base/create-resume.html', context)

# def updateResume(request, pk):
#     user = request.user
#     recruiter = Recruiter.objects.get(user=user)
#     resume = get_object_or_404(Resume, id=pk)
#     Resumeform = resumeForm(request.POST or None, instance = resume)
#     ExperienceFormset = modelformset_factory(Experience, form=experienceForm, extra=0)
#     ExperienceFormset = ExperienceFormset(request.POST or None)
#     #qs = recruiter.education_set.all()
#     context = {
#         "resume_form":Resumeform,
#         "experiencesForm":ExperienceFormset,
#         "user_data":recruiter,
#     }
    
#     if all([Resumeform.is_valid(), ExperienceFormset.is_valid()]):
#         print(request.POST)
#         parent = Resumeform.save(commit=False)
#         parent.save()
#         context['message'] = 'formset error'
#         for form in ExperienceFormset:
#             child = form.save(commit=False)
#             child.resume = parent
#             child.save()
#             context['message'] = 'Data Saved'

    
#     return render(request, 'base/update-resume.html', context)


def updateResume(request, pk):
    user = request.user
    recruiter = Recruiter.objects.get(user=user)
    resume = get_object_or_404(Resume, id=pk)
    Resumeform = resumeForm(request.POST or None, instance = resume)
    #data forms
    experiences = Experience.objects.filter(resume=resume)
    ExperienceForm = experienceForm(request.POST or None)
    education = Education.objects.filter(resume=resume)
    EducationForm = educationForm(request.POST or None)
    new_education_url = reverse("resume:hx-education-create", kwargs={"parent_id":pk})
    new_experience_url = reverse("resume:hx-experience-create", kwargs={"parent_id":pk})

    if Resumeform.is_valid():
        print(request.POST)
        parent = Resumeform.save(commit=False)
        parent.save()

    if ExperienceForm.is_valid():
        print(request)
        instance = ExperienceForm.save(commit=False)
        instance.resume = resume
        instance.save()
    
    if EducationForm.is_valid():
        print(request)
        instance = EducationForm.save(commit=False)
        instance.resume = resume
        instance.save()

    context = {
        "resume_form":Resumeform,
        "resume":resume,
        "experience_form":ExperienceForm,
        "education_form":EducationForm,
        "user_data":recruiter,
        "new_education_url":new_education_url,
        "new_experience_url":new_experience_url
    }
    if request.htmx:
        return render(request, "base/partials/experience_form.html", context)

    return render(request, 'base/update-resume.html', context)


def education_update_hx_view(request, parent_id=None, id=None):
    if not request.htmx:
        raise Http404
    try:
        parent_obj = Resume.objects.get(id=parent_id, user=request.user)
    except:
        parent_obj = None

    if parent_obj is  None:
        return HttpResponse("Not found.")

    instance = None

    if id is not None:
        try:
            instance = Education.objects.get(resume=parent_obj, id=id)
        except:
            instance = None
    form = educationForm(request.POST or None, instance=instance)
    url = reverse("resume:hx-education-create", kwargs={"parent_id":parent_id})

    if instance:
        url = instance.get_hx_edit_url()

    context = {
        "url":url,
        "form": form,
        "data": instance
    }
    if form.is_valid():
        new_obj = form.save(commit=False)
        if instance is None:
            new_obj.resume = parent_obj

        new_obj.save()
        context['data'] = new_obj
        return render(request, "base/partials/education_inline.html", context) 

    return render(request, "base/partials/education_form.html", context)

    
def experience_update_hx_view(request, parent_id=None, id=None):
    if not request.htmx:
        raise Http404
    try:
        parent_obj = Resume.objects.get(id=parent_id, user=request.user)
    except:
        parent_obj = None

    if parent_obj is  None:
        return HttpResponse("Not found.")

    instance = None

    if id is not None:
        try:
            instance = Experience.objects.get(resume=parent_obj, id=id)
        except:
            instance = None
    form = experienceForm(request.POST or None, instance=instance)
    url = reverse("resume:hx-experience-create", kwargs={"parent_id":parent_id})

    if instance:
        url = instance.get_hx_edit_url()

    context = {
        "url":url,
        "form": form,
        "data": instance
    }
    if form.is_valid():
        new_obj = form.save(commit=False)
        if instance is None:
            new_obj.resume = parent_obj

        new_obj.save()
        context['data'] = new_obj
        return render(request, "base/partials/experience_inline.html", context) 

    return render(request, "base/partials/experience_form.html", context)  


def experience_delete_view(request, parent_id=None, id=None):
    try:
        obj = Experience.objects.get(resume__id=parent_id, id=id, resume__user=request.user)
    except:
        obj = None

    if obj is None:
        if request.htmx:
            return HttpResponse("Not Found")
        raise Http404

    if request.method == "POST":
        obj.delete()
        success_url = reverse('resume:update-resume', kwargs={"id": parent_id})
        if request.htmx:
            return render(request, "base/partials/deleted_message.html")
        return redirect(success_url)
        
    context = {
        "object": obj
    }
    return render(request, "base/partials/deleted_message.html")

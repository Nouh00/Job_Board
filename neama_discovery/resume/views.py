from multiprocessing import context
from django.shortcuts import render, get_object_or_404, redirect
from django.forms.models import modelformset_factory
from django.http import HttpResponse, Http404
from .models import Resume, Education, Experience, Work, Publications, Urls, Skills
from .forms import resumeForm, educationForm, experienceForm, workForm, publicationsForm, urlsForm, skillsForm
from accounts.models import Recruiter, candidate
from django.urls import reverse





def resume(request, pk):
    resume = Resume.objects.filter(user__id=pk)
    recruiter = Recruiter.objects.get(user=request.user)
    if not resume:
        return redirect('resume:create-resume')

    resume = Resume.objects.get(user__id=pk)
    experiences = Experience.objects.filter(resume__id = resume.id)
    publications = Publications.objects.filter(resume__id = resume.id)
    work = Work.objects.filter(resume__id = resume.id)
    urls = Urls.objects.filter(resume__id = resume.id)
    education = Education.objects.filter(resume__id = resume.id)
    

    context = {
        'resume':resume,
        "experiences": experiences,
        "publications":publications,
        "work":work,
        "urls":urls,
        "education":education,
        "certificates":"",
        "user":recruiter
    }
    return render(request, 'base/resume.html', context)


def createResume(request):
    user = request.user
    recruiter = Recruiter.objects.get(user=user)
    resume = Resume.objects.get_or_create(user=user)[0]

    return redirect('resume:update-resume', pk=resume.id)

def updateResume(request, pk):
    user = request.user
    recruiter = Recruiter.objects.get(user=user)
    resume = Resume.objects.get_or_create(user=user)[0]
    Resumeform = resumeForm(request.POST or None, instance = resume)
    #data forms
    ExperienceForm = experienceForm(request.POST or None)
    EducationForm = educationForm(request.POST or None)
    new_education_url = reverse("resume:hx-education-create", kwargs={"parent_id":pk})
    new_experience_url = reverse("resume:hx-experience-create", kwargs={"parent_id":pk})
    new_work_url = reverse("resume:hx-work-create", kwargs={"parent_id":pk})
    new_publication_url = reverse("resume:hx-publication-create", kwargs={"parent_id":pk})
    new_url_url = reverse("resume:hx-url-create", kwargs={"parent_id":pk})
    new_skill_url = reverse("resume:hx-skill-create", kwargs={"parent_id":pk})

    
    if Resumeform.is_valid():
        print(request.POST)
        parent = Resumeform.save(commit=False)
        parent.save()

    context = {
        "resume":resume,
        "user_data":recruiter,

        "experience_form":ExperienceForm,
        "education_form":EducationForm,
        "resume_form":Resumeform,
        
        "new_education_url":new_education_url,
        "new_experience_url":new_experience_url,
        "new_work_url":new_work_url,
        "new_publication_url":new_publication_url,
        "new_url_url":new_url_url,
        "new_skill_url":new_skill_url,

    }

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


def education_delete_view(request, parent_id=None, id=None):
    try:
        obj = Education.objects.get(resume__id=parent_id, id=id, resume__user=request.user)
    except:
        obj = None

    if obj is None:
        if request.htmx:
            print(request.htmx)
            return HttpResponse("Not Found")
        raise Http404

    if request.method == "POST":
        obj.delete()
        success_url = reverse('resume:update-resume', kwargs={"pk": parent_id})
        if request.htmx:
            return render(request, "base/partials/deleted_message.html")
        return redirect(success_url)

    context = {
        "object": obj
    }
    return render(request, "base/partials/deleted_message.html")



    
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
            print(request.htmx)
            return HttpResponse("Not Found")
        raise Http404

    if request.method == "POST":
        obj.delete()
        success_url = reverse('resume:update-resume', kwargs={"pk": parent_id})
        if request.htmx:
            return render(request, "base/partials/deleted_message.html")
        return redirect(success_url)

    context = {
        "object": obj
    }
    return render(request, "base/partials/deleted_message.html")


def work_update_hx_view(request, parent_id=None, id=None):
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
            instance = Work.objects.get(resume=parent_obj, id=id)
        except:
            instance = None
    form = workForm(request.POST or None, instance=instance)
    url = reverse("resume:hx-work-create", kwargs={"parent_id":parent_id})

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
        return render(request, "base/partials/work_inline.html", context) 

    return render(request, "base/partials/work_form.html", context)

def work_delete_view(request, parent_id=None, id=None):
    try:
        obj = Work.objects.get(resume__id=parent_id, id=id, resume__user=request.user)
    except:
        obj = None

    if obj is None:
        if request.htmx:
            print(request.htmx)
            return HttpResponse("Not Found")
        raise Http404

    if request.method == "POST":
        obj.delete()
        success_url = reverse('resume:update-resume', kwargs={"pk": parent_id})
        if request.htmx:
            return render(request, "base/partials/deleted_message.html")
        return redirect(success_url)

    context = {
        "object": obj
    }
    return render(request, "base/partials/deleted_message.html")


    
def publication_update_hx_view(request, parent_id=None, id=None):
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
            instance = Publications.objects.get(resume=parent_obj, id=id)
        except:
            instance = None
    form = publicationsForm(request.POST or None, instance=instance)
    url = reverse("resume:hx-publication-create", kwargs={"parent_id":parent_id})

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
        return render(request, "base/partials/publication_inline.html", context) 

    return render(request, "base/partials/publication_form.html", context)

def publication_delete_view(request, parent_id=None, id=None):
    try:
        obj = Publications.objects.get(resume__id=parent_id, id=id, resume__user=request.user)
    except:
        obj = None

    if obj is None:
        if request.htmx:
            print(request.htmx)
            return HttpResponse("Not Found")
        raise Http404

    if request.method == "POST":
        obj.delete()
        success_url = reverse('resume:update-resume', kwargs={"pk": parent_id})
        if request.htmx:
            return render(request, "base/partials/deleted_message.html")
        return redirect(success_url)

    context = {
        "object": obj
    }
    return render(request, "base/partials/deleted_message.html")


def url_update_hx_view(request, parent_id=None, id=None):
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
            instance = Urls.objects.get(resume=parent_obj, id=id)
        except:
            instance = None
    form = urlsForm(request.POST or None, instance=instance)
    url = reverse("resume:hx-url-create", kwargs={"parent_id":parent_id})

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
        return render(request, "base/partials/urls_inline.html", context) 

    return render(request, "base/partials/urls_form.html", context)

def url_delete_view(request, parent_id=None, id=None):
    try:
        obj = Urls.objects.get(resume__id=parent_id, id=id, resume__user=request.user)
    except:
        obj = None

    if obj is None:
        if request.htmx:
            print(request.htmx)
            return HttpResponse("Not Found")
        raise Http404

    if request.method == "POST":
        obj.delete()
        success_url = reverse('resume:update-resume', kwargs={"pk": parent_id})
        if request.htmx:
            return render(request, "base/partials/deleted_message.html")
        return redirect(success_url)

    context = {
        "object": obj
    }
    return render(request, "base/partials/deleted_message.html")

def skill_update_hx_view(request, parent_id=None, id=None):
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
            instance = Skills.objects.get(resume=parent_obj, id=id)
        except:
            instance = None
    form = skillsForm(request.POST or None, instance=instance)
    url = reverse("resume:hx-skill-create", kwargs={"parent_id":parent_id})

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
        return render(request, "base/partials/skills_inline.html", context) 

    return render(request, "base/partials/skills_form.html", context)

def skill_delete_view(request, parent_id=None, id=None):
    try:
        obj = Skills.objects.get(resume__id=parent_id, id=id, resume__user=request.user)
    except:
        obj = None

    if obj is None:
        if request.htmx:
            print(request.htmx)
            return HttpResponse("Not Found")
        raise Http404

    if request.method == "POST":
        obj.delete()
        success_url = reverse('resume:update-resume', kwargs={"pk": parent_id})
        if request.htmx:
            return render(request, "base/partials/deleted_message.html")
        return redirect(success_url)

    context = {
        "object": obj
    }
    return render(request, "base/partials/deleted_message.html")

from django.urls import reverse
from datetime import date
from django.db import models
from django.contrib.auth.models import User
# Create your models here.


skill_set = (
    ("Photoshop", "Photoshop"),
    ("Python Development", "Python Development"),
    ("Excel", "Excel")
)

class Resume(models.Model):
    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE, related_name="user_cv")
    cv = models.FileField(null=True, blank=True)
    bio = models.CharField(max_length=500, null=True, blank=True,)
    skills = models.CharField(max_length=200, choices=skill_set, null=True)
    #certificates = models.ImageField()
    def get_education(self):
        return self.education_set.all()
    
    def get_experience(self):
        return self.experience_set.all()
    
    def get_work(self):
        return self.work_set.all()

    def get_publications(self):
        return self.publications_set.all()

    def get_urls(self):
        return self.urls_set.all()
    

class Education(models.Model):
    resume = models.ForeignKey(Resume,on_delete=models.CASCADE)
    degree = models.CharField(max_length=500, null=True, blank=True)
    major =models.CharField(max_length=500, null=True, blank=True)
    start_date = models.DateField()
    end_date= models.DateField()
    university = models.CharField(max_length=500, null=True, blank=True)
    wilaya = models.CharField(max_length=500, null=True, blank=True)
    description = models.CharField(max_length=500, null=True, blank=True)

    def get_hx_edit_url(self):
        kwargs= {
            "parent_id":self.resume.id,
            "id":self.id
        }

        return reverse("resume:hx-education-detail", kwargs=kwargs)

    

class Experience(models.Model):
    resume = models.ForeignKey(Resume,on_delete=models.CASCADE)
    title = models.CharField(max_length=500, null=True, blank=True)
    start_date = models.DateField()
    end_date= models.DateField()
    organization = models.CharField(max_length=500, null=True, blank=True)
    wilaya = models.CharField(max_length=500, null=True, blank=True)
    description = models.CharField(max_length=500, null=True, blank=True)
    def get_hx_edit_url(self):
        kwargs= {
            "parent_id":self.resume.id,
            "id":self.id
        }

        return reverse("resume:hx-experience-detail", kwargs=kwargs)
    
    def get_hx_delete_url(self):
        kwargs= {
            "parent_id":self.resume.id,
            "id":self.id
        }

        return reverse("resume:hx-experience-delete", kwargs=kwargs)

class Work(models.Model):
    resume = models.ForeignKey(Resume,on_delete=models.CASCADE)
    title = models.CharField(max_length=500, null=True, blank=True)
    start_date = models.DateField()
    end_date= models.DateField()
    organization = models.CharField(max_length=500, null=True, blank=True)
    wilaya = models.CharField(max_length=500, null=True, blank=True)
    description = models.CharField(max_length=500, null=True, blank=True)
    def get_hx_edit_url(self):
        kwargs= {
            "parent_id":self.resume.id,
            "id":self.id
        }

        return reverse("resume:hx-education-detail", kwargs=kwargs)

class Publications(models.Model):
    resume = models.ForeignKey(Resume,on_delete=models.CASCADE)
    title = models.CharField(max_length=500, null=True, blank=True)
    date = models.DateField()
    publisher = models.CharField(max_length=500, null=True, blank=True)
    journal = models.CharField(max_length=500, null=True, blank=True)
    description = models.CharField(max_length=500, null=True, blank=True)
    def get_hx_edit_url(self):
        kwargs= {
            "parent_id":self.resume.id,
            "id":self.id
        }

        return reverse("resume:hx-education-detail", kwargs=kwargs)

class Urls(models.Model):
    resume = models.ForeignKey(Resume,on_delete=models.CASCADE)
    website = models.CharField(max_length=500, null=True, blank=True)
    url = models.URLField(max_length=500)
    def get_hx_edit_url(self):
        kwargs= {
            "parent_id":self.resume.id,
            "id":self.id
        }

        return reverse("resume:hx-education-detail", kwargs=kwargs)
from django.contrib import admin
from .models import Resume, Education, Experience, Skills, Work, Publications, Urls
# Register your models here.


class educationInline(admin.StackedInline):
    model = Education
    extra = 0


class experienceInline(admin.StackedInline):
    model = Experience
    extra = 0
    

class workInline(admin.StackedInline):
    model = Work
    extra = 0
    

class publicationsInline(admin.StackedInline):
    model = Publications
    extra = 0
    

class urls(admin.StackedInline):
    model = Urls
    extra = 0

class skills(admin.StackedInline):
    model = Skills
    extra = 0
    

class ResumeInlines(admin.ModelAdmin):
    inlines = [
        educationInline,
        experienceInline,
        workInline,
        publicationsInline,
        urls,
        skills,
        ]
    list_display = ['bio']
    raw_id_fields = ['user']
    



admin.site.register(Resume, ResumeInlines)
#admin.site.register(Skills)
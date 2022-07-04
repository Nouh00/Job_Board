import imp
from django.contrib import admin
from .models import Category, Opportunity, Applicant

# Register your models here.
admin.site.register(Category)
admin.site.register(Opportunity)
admin.site.register(Applicant)
from django.db import models
from django.contrib.auth.models import User
from companies.models import Company
# Create your models here.
OPPORTUNITY_TYPE = (
    ('1', "Full time"),
    ('2', "Part time"),
    ('3', "Internship"),
)
class Category(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Opportunity(models.Model):

    user = models.ForeignKey(User, related_name='user' ,on_delete=models.SET_NULL, null=True) 
    title = models.CharField(max_length=300)
    description = models.TextField(max_length=500, null=True, blank=True)
    #tags = TaggableManager()
    location = models.CharField(max_length=300)
    opportunity_type = models.CharField(choices=OPPORTUNITY_TYPE, max_length=1, blank=True)
    category = models.ForeignKey(Category,related_name='Category', on_delete=models.CASCADE)
    salary = models.CharField(max_length=30, blank=True)
    company = models.ForeignKey(Company, related_name='company' ,on_delete=models.SET_NULL, null=True)  
    url = models.URLField(max_length=200)
    deadline = models.DateField()
    is_published = models.BooleanField(default=False)
    is_closed = models.BooleanField(default=False)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)
    applicants = models.ManyToManyField(User, null=True, through='Applicant')


    def __str__(self):
        return self.title


class Applicant(models.Model):

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    opportunity = models.ForeignKey(Opportunity, on_delete=models.CASCADE)
    applied = models.DateTimeField(auto_now=True, auto_now_add=False)


    def __str__(self):
        return self.user.email
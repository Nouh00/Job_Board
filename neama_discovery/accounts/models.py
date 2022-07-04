from email.policy import default
from http.client import MULTIPLE_CHOICES
from random import choices
from django.db import models
from django.contrib.auth.models import User


ROLE = (
    ('recruiter', "Recruiter"),
    ('volunteer', "Volunteer"),
)

GENDER = (
    ('M', "Male"),
    ('F', "Female"),

)

class Recruiter(models.Model):
    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    fname = models.CharField(max_length=200, null=True)
    lname = models.CharField(max_length=200, null=True)
    gender = models.CharField(choices=GENDER, max_length=1, null=True)
    phone = models.CharField(max_length=200, null=True)
    email = models.CharField(max_length=200, null=True)
    adresse = models.CharField(max_length=200, null=True)
    birth = models.DateField(null=True)
    date_created = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return self.fname

    def full_name(self):
        return self.first_name+ ' ' + self.last_name

class candidate(models.Model):
    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    #profile_pic
    fname = models.CharField(max_length=200, null=True)
    lname = models.CharField(max_length=200, null=True)
    gender = models.CharField(choices=GENDER, max_length=1, null=True)
    phone = models.CharField(max_length=200, null=True)
    email = models.CharField(max_length=200, null=True)
    adresse = models.CharField(max_length=200, null=True)
    birth = models.DateField(null=True)
    date_created = models.DateTimeField(auto_now_add=True, null=True)

    

    def __str__(self):
        return self.fname

    def full_name(self):
        return self.first_name+ ' ' + self.last_name

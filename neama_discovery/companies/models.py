from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Company(models.Model):
    user = models.ForeignKey(User,on_delete=models.SET_NULL, null=True,)
    name = models.CharField(max_length=300)
    location = models.CharField(max_length=300)
    description = models.TextField(max_length=500, null=True, blank=True)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)
    is_published = models.BooleanField(default=False)

    def __str__(self):
        return self.name
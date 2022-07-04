from operator import imod
from tkinter import Widget
from django.forms import ModelForm
from .models import Recruiter, candidate



class candidateForm(ModelForm):

    class Meta:
        model = candidate
        fields = '__all__'
        exclude = ['user']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields:
            styling={
                "class" : "block w-full px-4 py-2 mt-2 text-gray-700 bg-white border border-gray-200 rounded-md   focus:border-blue-400 focus:ring-blue-300 focus:ring-opacity-40 focus:outline-none focus:ring"
            }
            self.fields[str(field)].widget.attrs.update(
                styling
            )

class recruiterForm(ModelForm):

    class Meta:
        model = Recruiter
        fields = '__all__'
        exclude = ['user']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields:
            styling={
                "class" : "block w-full px-4 py-2 mt-2 text-gray-700 bg-white border border-gray-200 rounded-md   focus:border-blue-400 focus:ring-blue-300 focus:ring-opacity-40 focus:outline-none focus:ring"
            }
            self.fields[str(field)].widget.attrs.update(
                styling
            )

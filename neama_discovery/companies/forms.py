import email
from django.forms import ModelForm
from .models import Company
from django.contrib.auth.forms import UserCreationForm


class createCompanyForm(ModelForm):

    class Meta:
        model = Company
        fields = '__all__'
        exclude = ['user','created', 'is_published']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields:
            styling={
                "class" : "block w-full px-4 py-2 mt-2 text-gray-700 bg-white border border-gray-200 rounded-md   focus:border-blue-400 focus:ring-blue-300 focus:ring-opacity-40 focus:outline-none focus:ring"
            }
            self.fields[str(field)].widget.attrs.update(
                styling
            )
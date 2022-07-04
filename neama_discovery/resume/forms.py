from django import forms
from django.forms import ModelForm, inlineformset_factory
from .models import Resume, Education, Experience, Work, Publications, Urls


class resumeForm(forms.ModelForm):
    class Meta:
        model = Resume
        fields = '__all__'
        exclude = ['user','cv']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields:
            styling={
                "class" : "block w-full px-4 py-2 mt-2 text-gray-700 bg-white border border-gray-200 rounded-md   focus:border-blue-400 focus:ring-blue-300 focus:ring-opacity-40 focus:outline-none focus:ring"
            }
            self.fields[str(field)].widget.attrs.update(
                styling
            )


class educationForm(forms.ModelForm):

    class Meta:
        model = Education
        fields = '__all__'
        exclude = ['resume']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields:
            styling={
                "class" : "block w-full px-4 py-2 mt-2 text-gray-700 bg-white border border-gray-200 rounded-md   focus:border-blue-400 focus:ring-blue-300 focus:ring-opacity-40 focus:outline-none focus:ring"
            }
            self.fields[str(field)].widget.attrs.update(
                styling
            )



class experienceForm(forms.ModelForm):

    class Meta:
        model = Experience
        fields = '__all__'
        exclude = ['resume']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields:
            styling={
                "class" : "block w-full px-4 py-2 mt-2 text-gray-700 bg-white border border-gray-200 rounded-md   focus:border-blue-400 focus:ring-blue-300 focus:ring-opacity-40 focus:outline-none focus:ring"
            }
            self.fields[str(field)].widget.attrs.update(
                styling
            )

ExperienceFormSet = inlineformset_factory(
    Resume,
    Experience,
    experienceForm,
    can_delete=True,
    extra=0
)

class workForm(forms.ModelForm):

    class Meta:
        model = Work
        fields = '__all__'
        exclude = ['resume']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields:
            styling={
                "class" : "block w-full px-4 py-2 mt-2 text-gray-700 bg-white border border-gray-200 rounded-md   focus:border-blue-400 focus:ring-blue-300 focus:ring-opacity-40 focus:outline-none focus:ring"
            }
            self.fields[str(field)].widget.attrs.update(
                styling
            )

class publicationsForm(forms.ModelForm):

    class Meta:
        model = Publications
        fields = '__all__'
        exclude = ['resume']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields:
            styling={
                "class" : "block w-full px-4 py-2 mt-2 text-gray-700 bg-white border border-gray-200 rounded-md   focus:border-blue-400 focus:ring-blue-300 focus:ring-opacity-40 focus:outline-none focus:ring"
            }
            self.fields[str(field)].widget.attrs.update(
                styling
            )

class urlsForm(forms.ModelForm):

    class Meta:
        model = Urls
        fields = '__all__'
        exclude = ['resume']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields:
            styling={
                "class" : "block w-full px-4 py-2 mt-2 text-gray-700 bg-white border border-gray-200 rounded-md   focus:border-blue-400 focus:ring-blue-300 focus:ring-opacity-40 focus:outline-none focus:ring"
            }
            self.fields[str(field)].widget.attrs.update(
                styling
            )


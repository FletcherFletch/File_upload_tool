from django import forms
from .models import uupload

class ImageForm(forms.ModelForm):
    class Meta:
        model = uupload
        fields = ['name', 'image', 'description']

    def clean_name(self):
        name = self.cleaned_data['name']
        if any(char.isdigit() for char in name):
            raise forms.ValidationError("Name cannot have numbers.")
        return name 
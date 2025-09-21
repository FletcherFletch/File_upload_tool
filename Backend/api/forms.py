from django import forms
from .models import uupload

class ImageForm(forms.ModelForm):
    class Meta:
        model = uupload
        fields = ['name', 'image', 'description']
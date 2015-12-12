from django import forms

from .models import Resource


class ResourceForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        pass

    class Meta:
        fields = ('url', 'name', 'description', 'added_by')
        model = Resource
        widgets = {
            'url': forms.URLInput(attrs={'class': 'form-control'}),
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control'}),
        }
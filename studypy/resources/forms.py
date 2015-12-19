from django import forms

from django_select2.forms import Select2MultipleWidget

from tags.models import Tag
from .models import Resource


class ResourceForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('added_by', None)
        kwargs['initial'] = {'added_by': self.user}
        super(ResourceForm, self).__init__(*args, **kwargs)

    def clean(self):
        cleaned_data = super(ResourceForm, self).clean()
        user = cleaned_data['added_by']
        if user != self.user:
            raise forms.ValidationError("Dont change hidden fields")

    class Meta:
        fields = ('url', 'name', 'description', 'added_by')
        model = Resource
        widgets = {
            'url': forms.URLInput(attrs={'class': 'form-control'}),
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control'}),
        }


class UpdateResourceForm(forms.ModelForm):
    class Meta:
        fields = ('url', 'name', 'description')
        model = Resource
        widgets = {
            'url': forms.URLInput(attrs={'class': 'form-control'}),
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control'}),
        }


class ResourceFilterForm(forms.Form):
    tags = forms.ModelMultipleChoiceField(queryset=Tag.objects.all(),
                                          widget=Select2MultipleWidget())

    class Media:
        js = ('js/resources/filter-form.js', )

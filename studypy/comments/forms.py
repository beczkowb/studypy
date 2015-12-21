from django import forms

from .models import ResourceComment


class ResourceCommentForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        self.author = kwargs.pop('author', None)
        self.resource = kwargs.pop('resource', None)
        super(ResourceCommentForm, self).__init__(*args, **kwargs)

    def clean(self):
        cleaned_data = super(ResourceCommentForm, self).clean()
        if self.author != cleaned_data['author'] or self.resource != cleaned_data['resource']:
            raise forms.ValidationError('Dont change hidden fields!')

    class Meta:
        model = ResourceComment
        fields = ('author', 'contents', 'resource')
        widgets = {
            'contents': forms.Textarea(attrs={'class': 'form-control',
                                              'style': 'height: 70px'}),
            'author': forms.HiddenInput(),
            'resource': forms.HiddenInput(),
        }
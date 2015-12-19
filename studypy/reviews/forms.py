from django import forms

from .models import Review


class ReviewForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('author', None)
        self.resource = kwargs.pop('resource', None)
        kwargs['initial'] = {'author': self.user, 'resource': self.resource}
        super(ReviewForm, self).__init__(*args, **kwargs)

    def clean(self):
        cleaned_data = super(ReviewForm, self).clean()
        user = cleaned_data['author']
        if user != self.user:
            raise forms.ValidationError("Dont change hidden fields")

    class Meta:
        model = Review
        fields = ('contents', 'mark', 'resource', 'author')
        widgets = {
            'contents': forms.Textarea(attrs={'class': 'form-control'}),
            'mark': forms.Select(attrs={'class': 'form-control'}),
        }


class UpdateReviewForm(forms.ModelForm):
    class Meta:
        fields = ('contents', 'mark')
        model = Review
        widgets = {
            'contents': forms.Textarea(attrs={'class': 'form-control'}),
        }
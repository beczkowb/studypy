from django import forms
from django.contrib.auth import authenticate, login, get_user_model


class LoginForm(forms.Form):
    username = forms.CharField(max_length=30, label='username')
    password = forms.CharField(max_length=30, label='password',
                               widget=forms.PasswordInput)

    def clean(self):
        cleaned_data = super(LoginForm, self).clean()
        username = cleaned_data.get('username')
        password = cleaned_data.get('password')
        user = authenticate(username=username, password=password)
        self.user = user
        if not user:
            raise forms.ValidationError("Invalid credentials, please try again")

    def login(self, request):
        username = self.cleaned_data['username']
        password = self.cleaned_data['password']
        login(request, self.user)


class UserProfileForm(forms.ModelForm):
    class Meta:
        model = get_user_model()
        fields = ('first_name', 'last_name', 'email', 'image')
        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'form-control'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
        }

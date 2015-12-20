from django import forms
from django.contrib.auth import authenticate, login, get_user_model
from django.contrib.auth.forms import UserCreationForm


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
            raise forms.ValidationError(
                "Invalid credentials, please try again")

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


class RegisterForm(UserCreationForm):
    password1 = forms.CharField(label="Password",
                                widget=forms.PasswordInput(attrs={
                                    'class': 'form-control'}))
    password2 = forms.CharField(label="Password confirmation",
                                widget=forms.PasswordInput(attrs={
                                    'class': 'form-control'}),
                                help_text="Enter the same password as above, for verification.")

    class Meta:
        model = get_user_model()
        fields = ('email', 'username',)
        widgets = {
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'username': forms.TextInput(attrs={'class': 'form-control'}),
        }

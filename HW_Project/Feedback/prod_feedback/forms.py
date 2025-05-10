from django import forms
from .models import Feed_back , User

class AddFeedbackForm(forms.ModelForm):
    class Meta:
        model = Feed_back
        fields = ['name', 'email', 'mobile', 'rating', 'message']


class UserRegistrationForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput, label="Password")
    password_confirm = forms.CharField(widget=forms.PasswordInput, label="Confirm Password")

    class Meta:
        model = User
        fields = ['email', 'name']

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get("password")
        password_confirm = cleaned_data.get("password_confirm")
        email = cleaned_data.get("email")

        if password and password_confirm and password != password_confirm:
            raise forms.ValidationError("Passwords do not match.")

        if email and User.objects.filter(email=email).exists():
            raise forms.ValidationError("A user with this email already exists.")

        return cleaned_data


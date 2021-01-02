from django.core import validators
from django import forms
from enroll.models import student
from django.core.exceptions import ValidationError

class StudentRegistration(forms.ModelForm):
    class Meta:
        model = student
        fields = ['name', 'email', 'password']
        widgets = {
             'name':forms.TextInput(attrs={'class':'form-control'}),
             'email':forms.EmailInput(attrs={'class':'form-control'}),
             'password':forms.PasswordInput(render_value=True, attrs={'class':'form-control'}),
         }

    def clean_email(self):
        email = self.cleaned_data.get('email')
        for instance in student.objects.all():
            if instance.email == email:
                raise forms.ValidationError("Email Already Registered")
        return email


class StudentRegistrationUpdate(forms.ModelForm):
    class Meta:
        model = student
        fields = ['name', 'email', 'password']
        widgets = {
             'name':forms.TextInput(attrs={'class':'form-control'}),
             'email':forms.EmailInput(attrs={'class':'form-control'}),
             'password':forms.PasswordInput(render_value=True, attrs={'class':'form-control'}),
         }
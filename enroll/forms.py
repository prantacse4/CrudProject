from django.core import validators
from django import forms
from enroll.models import student
from django.core.exceptions import ValidationError

class StudentRegistration(forms.ModelForm):
    class Meta:
        model = student
        fields = ['name', 'email', 'password']

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
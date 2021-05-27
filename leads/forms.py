from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm, UsernameField

from leads.models import Lead

User = get_user_model()


class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = '__all__'
        field_classes = {'username': UsernameField}


class LeadModelForm(forms.ModelForm):
    class Meta:
        model = Lead
        fields = (
            "first_name",
            "last_name",
            "age",
            "agent",
        )

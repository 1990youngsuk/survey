from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User

from .models import *


class SurveyForm(ModelForm):

    class Meta:
        model = Survey
        fields = '__all__'

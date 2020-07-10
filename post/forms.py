from django import forms
from django.forms import ModelForm

from .models import *

class CodeForm(forms.ModelForm):
    class Meta:
        model = CodeModel
        fields = '__all__'
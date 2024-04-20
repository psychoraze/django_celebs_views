from django import forms
from .models import *


class CelebrityForm(forms.ModelForm):
    class Meta:
        model = Celebrity
        fields = ["name", "age", "films", "capital"]

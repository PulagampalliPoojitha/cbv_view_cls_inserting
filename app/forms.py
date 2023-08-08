from django import forms
from app.models import *
class StudentForm(forms.ModelForm):
    class Meta:
        model=student
        fields='__all__'

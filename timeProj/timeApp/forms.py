from django import forms
from .models import TimeModel

# FORM TO SYNC MODEL INFO
class TimeForm(forms.ModelForm):
    class Meta:
        model= TimeModel
        fields = ['teachName', 'school', 'subject','workDate', 'hours']

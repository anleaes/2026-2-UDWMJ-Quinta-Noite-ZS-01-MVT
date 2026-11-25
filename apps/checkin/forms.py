from django import forms
from .models import CheckIn

class CheckInForm(forms.ModelForm):

    class Meta:
        model = CheckIn
        exclude = ()

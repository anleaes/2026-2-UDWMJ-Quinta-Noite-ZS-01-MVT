from django import forms
from .models import Atracao

class AtracaoForm(forms.ModelForm):

    class Meta:
        model = Atracao
        exclude = ()

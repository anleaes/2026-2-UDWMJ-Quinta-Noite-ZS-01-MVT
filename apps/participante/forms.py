from django import forms
from .models import Participante

class ParticipanteForm(forms.ModelForm):

    class Meta:
        model = Participante
        exclude = ()
        widgets = {
            'data_nascimento': forms.DateInput(attrs={'type': 'date'}, format='%Y-%m-%d'),
        }

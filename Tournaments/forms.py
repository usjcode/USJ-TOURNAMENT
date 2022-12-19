from .models import Tournament
from django import  forms
from .models import Tournament,WritingSession,OralSession


class AddTournamentForm(forms.ModelForm):
    class Meta:
        model=Tournament
        fields=("__all__")
    
    
    

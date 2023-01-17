from .models import Tournament
from django import  forms
from .models import Tournament,WritingSession,OralSession


class AddTournamentForm(forms.ModelForm):
    class Meta:
        model=Tournament
        fields=("__all__")
        widgets={
            "date_inscription":forms.DateInput(attrs={"type":"date"})
        }
        
        
class UpdateTournamentForm(forms.ModelForm):
    class Meta:
        model=Tournament
        fields=("description","date_inscription")
        widgets={
            "date_inscription":forms.DateInput(attrs={"type":"date"})
        }
        
    
    
    

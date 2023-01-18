from .models import Tournament
from django import  forms
from .models import Tournament,WritingSession,OralSession


class AddTournamentForm(forms.ModelForm):
    class Meta:
        model=Tournament
        exclude=("date_annonce",)
        widgets={
            "date_inscription":forms.DateInput(attrs={"type":"date"}),
            "date_debut":forms.DateInput(attrs={"type":"date"}),
        }
        
        
class UpdateTournamentForm(forms.ModelForm):
    class Meta:
        model=Tournament
        fields=("description","date_inscription","date_debut")
        widgets={
            "date_inscription":forms.DateInput(attrs={"type":"date"}),
            "date_debut":forms.DateInput(attrs={"type":"date"}),

        }
        
    
    
    

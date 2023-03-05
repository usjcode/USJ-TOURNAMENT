from .models import Tournament
from django import  forms
from .models import Tournament,WritingSession,OralSession
from rest_framework import serializers

class TournamentSerializer(serializers.ModelSerializer):
    class Meta:
        class Meta:
            model=Tournament
        exclude=("date_annonce",)
        widgets={
            "date_inscription":forms.DateInput(attrs={"type":"date"}),
            "date_debut":forms.DateInput(attrs={"type":"date"}),
        }



# class AddTournamentForm(forms.ModelForm):
#     class Meta:
#         model=Tournament
#         exclude=("date_annonce",)
#         widgets={
#             "date_inscription":forms.DateInput(attrs={"type":"date"}),
#             "date_debut":forms.DateInput(attrs={"type":"date"}),
#         }
        
        
# class UpdateTournamentForm(forms.ModelForm):
#     class Meta:
#         model=Tournament
#         fields=("description","date_inscription","date_debut")
#         widgets={
#             "date_inscription":forms.DateInput(attrs={"type":"date"}),
#             "date_debut":forms.DateInput(attrs={"type":"date"}),

#         }
        
    
    
    

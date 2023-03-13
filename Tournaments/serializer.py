from .models import Tournament
from django import  forms
from .models import Tournament,WritingSession,OralSession
from rest_framework import serializers

class TournamentSerializer(serializers.ModelSerializer):
    class Meta:
        model=Tournament
        exclude=["date_annonce"]
    




from .models import Tournament
from candidate.models import Candidacy
from rest_framework import serializers

class TournamentSerializer(serializers.ModelSerializer):
    class Meta:
        model=Tournament
        exclude=["date_annonce"]

class TournamentCandidateSerializer(serializers.ModelSerializer):
        class Meta:
            model = Candidacy
            fields=('anonymat_number',)
    




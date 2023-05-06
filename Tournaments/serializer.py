import datetime
from .models import Tournament
from candidate.models import Candidacy
from rest_framework import serializers
from django.db.models.functions import Now


from rest_framework.exceptions import ValidationError

class TournamentSerializer(serializers.ModelSerializer):
    class Meta:
        model=Tournament
        exclude=["date_annonce"]
    def validate(self, data):
        if self.instance:
            if Tournament.objects.filter(date_inscription__gt=Now(),type=data.get("type")).exists():
                raise ValidationError(detail='il existe encore un concours de meme type déja en cours  modifié les données de l\'ancien')
        if  (data.get("nbr_place") or 0) > 200:
            raise ValidationError(detail='le nombre de place ne doit pas etre supérieur a 200')
        if datetime.date.today() >=data["date_inscription"]:
            raise ValidationError(detail="vous ne pouvez pas definir une date d'inscription qui est déja passé")
        if data["date_inscription"] >=data["date_debut"]:
            raise ValidationError(detail="vous ne pouvez pas definir une date de début de concours qui est avant la date de début")

        return data

class TournamentCandidateSerializer(serializers.ModelSerializer):
        class Meta:
            model = Candidacy
            fields=('anonymat_number',)
    




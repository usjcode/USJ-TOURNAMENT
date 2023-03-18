from .models import Candidacy,WritingNote,OralNote
from rest_framework import serializers

from rest_framework import serializers
from django.contrib.auth.models import User
from django.contrib.auth.password_validation import validate_password
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework.validators import UniqueValidator
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
        
        
class CandidateSerializer(serializers.ModelSerializer):
        class Meta:
            model = Candidacy
            exclude=('anonymat_number',)
            depth = 1

class WritingNoteSerializer(serializers.ModelSerializer):
        class Meta:
            model = WritingNote
            fields=["matiere","note"]
            

class OralNoteSerializer(serializers.ModelSerializer):
        class Meta:
            model = OralNote
            fields=["matiere","note","observation"]
           
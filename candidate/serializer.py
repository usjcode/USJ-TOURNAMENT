from .models import Candidacy
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
        exclude=('tournament','anonymat_number')
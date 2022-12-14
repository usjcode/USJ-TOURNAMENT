from django.db import models
from Tournaments.models import Tournament

# Create your models here.

class Candidacy(models.Model):
    name = models.CharField(max_length=100,null=True)
    email = models.EmailField(max_length=100,null=True)
    birth_date= models.DateField(null=True)
    sex=models.CharField(max_length=1,null=True)
    phone = models.CharField(max_length=100,null=True)
    cni_number = models.CharField(max_length=10000,null=True)
    
    

class Candidate(models.Model):
    tournaments=models.ManyToManyField(Tournament)
    anonymat_number=models.IntegerField(null=True)
    
class Note (models.Model):
    matiere=models.CharField(max_length=100,null=True)
    valeur=models.models.IntegerField()


    
    
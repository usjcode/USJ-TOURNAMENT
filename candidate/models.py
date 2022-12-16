from django.db import models
from Tournaments.models import Tournament

# Create your models here.

class Candidacy(models.Model):
    SEX=[
        ("M","masculin"),
        ("F","masculin")
        
        ]
    
    DIPLOMES=[
        
    ]
    photo= models.ImageField(null=True)
    name = models.CharField(max_length=100,null=True)
    lastname= models.CharField(max_length=100,null=True)
    sex=models.CharField(max_length=1,null=True)
    birth_date= models.DateField(null=True)
    nationality=models.CharField(null=True,max_length=100)
    
    email = models.EmailField(max_length=100,null=True)

    phone = models.CharField(max_length=100,null=True)
    cni_number = models.CharField(max_length=1000,null=True)
    photo_recto_cni=models.ImageField(upload_to="cni",null=True)
    photo_verso_cni=models.ImageField(upload_to="cni",null=True)
    
    def __str__(self):
        return  self.name+' ' + self.lastname + ' :' + self.cni_number
    
        
    
    
    
    

class Candidate(models.Model):
    tournament=models.ForeignKey(Tournament, on_delete=models.CASCADE,null=True)
    anonymat_number=models.IntegerField(null=True)
    
class Notee(models.Model):
    matiere=models.CharField(max_length=100,null=True)
    valeur=models.IntegerField()

class Noteo(models.Model):
    pass
    

    
    
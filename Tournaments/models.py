from django.db import models
from django.utils.translation import gettext_lazy as _
from django.core.exceptions import ValidationError
# Create your models here.
from django import forms
from django.db.models.functions import Now

import datetime


    
class TournamentType(models.Model):
    nom=models.CharField(primary_key=True,max_length=140)
    color=models.CharField(default="#00f",max_length=140)
    def __str__(self) -> str:
        return self.nom
    
class TournamentSubject(models.Model):
    name=models.CharField(primary_key=True,max_length=140)
    tournaments=models.ManyToManyField(TournamentType)
    def __str__(self) -> str:
        return self.name
class Tournament(models.Model):

    type = models.ForeignKey(TournamentType,on_delete=models.CASCADE)    
    description=models.TextField(null=True,blank=True)
    date_annonce=models.DateField(auto_now_add=True)
    #date limite d'inscription
    date_inscription=models.DateField(null=True,verbose_name="date limite d'inscription")
    
    date_debut=models.DateField(null=True,verbose_name="date de d'ébut")
    # nombre de place pour le concour
    nbr_place=models.IntegerField(default=50,verbose_name="nombre maximum de place")  
    
    def __str__(self):
        return  self.type.nom + str(self.date_annonce)
        
    def clean(self):
        if self.pk ==None:
            if  Tournament.objects.filter(date_inscription__gt=Now(),type=self.type).exists():
                raise ValidationError({'type': _('il existe encore un concours de meme type déja en cours  modifié les données de l\'ancien')})
            elif  self.nbr_place > 200:
                raise ValidationError({'nbr_place': _('le nombre de place ne doit pas etre supérieur a 200')})
            elif datetime.date.today() >=self.date_inscription:
                raise ValidationError({'date_inscription': _("vous ne pouvez pas definir une date d'inscription qui est déja passé")})

                
            

  
    def save(self, *args, **kwargs):
        if  not self.description:
            if self.type.nom=='cl1i':
                self.description="""rejoignez nous et  obtenez une licence professionelle 
                d'ans le develloppement d'application pour l'economie numerique"""
            elif self.type.nom=='cl1m':
                self.description="""spécialiser vous en management"""
            elif self.type=='cing1i':
                self.description="""suivez dès mintenant un formation d'ingenieur en nformatique chez nous !"""
            elif self.type.nom=='cing3i':
                self.description.nom=""" specialisez vous dans l'ingénieurie informatique"""
            else :
                self.description="""spécialiser vous en (data science ,securité, et systeme d'information)"""

        super().save(*args, **kwargs)
          


    


    
    
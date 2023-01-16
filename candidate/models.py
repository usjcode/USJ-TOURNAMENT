from django.db import models
from Tournaments.models import Tournament

# Create your models here.


class Candidacy(models.Model):
    SEX=[
        ("M","masculin"),
        ("F","masculin")
        
        ]
    
    classes=[
        ("autre","autre"),  
        ("sizieme","sizieme"),
        ("cinquieme","cinquieme"),
        ("quatrieme","quatrieme"),
        ("troizieme","troizieme"),
        ("seconde","seconde"),
        ("pemiere","premiere"),
        ("terminale","terminale")
        
    ]
    
    
    tournament=models.ForeignKey(Tournament, on_delete=models.CASCADE,null=True)
    anonymat_number=models.IntegerField(null=True)
    name = models.CharField(max_length=100,null=True)
    lastname= models.CharField(max_length=100,null=True)
    photo= models.ImageField(null=True,blank=True)
    sex=models.CharField(max_length=1,default='M',verbose_name="votre sex",choices=SEX)
    birth_date= models.DateField(null=True)
    birth_place=models.CharField(max_length=100,null=True)
    bacc=models.BooleanField(default=True)
    obtentionyear=models.IntegerField(default=2022,verbose_name="année d'obtention",null=True)
    exschool=models.CharField(max_length=100,null=True,verbose_name="votre établissement")
    hasrepeated=models.BooleanField(default=False,verbose_name="avez vous déja redoublé ?")
    repeatedclasse=models.CharField(null="terminale",blank=True,max_length=50,verbose_name="classe repété",choices=classes)
    mention=models.CharField(default="passable",max_length=100)
    examcenter=models.CharField(default="yaoundé",verbose_name="centre d'examination",max_length=100)
    exschoolcity=models.CharField(max_length=100,null=True,verbose_name="ville de votre établissement")
    series=models.CharField(default="E",max_length=10,verbose_name="votre série")
    
    nationality=models.CharField(null=True,max_length=100)
    
    email = models.EmailField(max_length=100,null=True)
    baccmark=models.IntegerField(default=10,verbose_name="moyenne générale au bacc")
    probatoiremark=models.IntegerField(default=10,verbose_name="moyenne générale au probatoire")
    phone = models.CharField(max_length=100,null=True,verbose_name="téléphone")
    region=models.CharField(max_length=100,null=True)
    adresse=models.CharField(max_length=100,null=True)
    cni_number = models.CharField(max_length=1000,null=True,verbose_name="numéro de cni")

    nompere=models.CharField(max_length=100,null=True,verbose_name="nom de la mere")
    nommere=models.CharField(max_length=100,null=True,verbose_name="nom du pere")
    professionmere=models.CharField(max_length=100,null=True,verbose_name="profession de la mere")
    professionpere=models.CharField(max_length=100,null=True,verbose_name="profession du père")
    situation=models.CharField(max_length=100,default="mariées")
    nombreenfant=models.IntegerField(default=1,verbose_name="nombre d'enfant")
    nombreenfantes=models.IntegerField(default=0,verbose_name="nombre d'enfant en etudes superieur")
    adresseparent=models.CharField(null=True,max_length=100,verbose_name="adresse des parents")

    photo_recto_cni=models.ImageField(upload_to="cni",null=True,blank=True)
    photo_verso_cni=models.ImageField(upload_to="cni",null=True,blank=True)
    
    def __str__(self):
        return  self.name+' ' + self.lastname + ' :' + self.cni_number
    
        
class Notee(models.Model):
    matiere=models.CharField(max_length=100,null=True)
    valeur=models.IntegerField()

class Noteo(models.Model):
    pass
    

    
    
from django.db import models
from Tournaments.models import Tournament, TournamentSubject

# Create your models here.


class Candidacy(models.Model):
    tournament=models.ForeignKey(Tournament, on_delete=models.CASCADE)
    anonymat_number=models.CharField(null=True,max_length=6,blank=True)
    name = models.CharField(max_length=100,null=True,verbose_name="nom")
    lastname= models.CharField(max_length=100,null=True,verbose_name="prenom")
    photo= models.ImageField(null=True,blank=True)
    sex=models.CharField(max_length=1,default='M',verbose_name="votre sex")
    birth_date= models.DateField(null=True,verbose_name="date de naissance")
    birth_place=models.CharField(max_length=100,null=True,verbose_name="lieu de naissance")
    bacc=models.BooleanField(default=True,verbose_name="avez vous le baccaléaurat??")
    obtentionyear=models.IntegerField(default=2022,verbose_name="année d'obtention",null=True)
    exschool=models.CharField(max_length=100,null=True,verbose_name="votre établissement")
    hasrepeated=models.BooleanField(default=False,verbose_name="avez vous déja redoublé ?")
    repeatedclasse=models.CharField(null="terminale",blank=True,max_length=50,verbose_name="classe repété")
    mention=models.CharField(default="passable",max_length=100)
    examcenter=models.CharField(default="yaoundé",verbose_name="centre d'examination",max_length=100)
    exschoolcity=models.CharField(max_length=100,null=True,verbose_name="ville de votre établissement")
    series=models.CharField(default="c",max_length=10,verbose_name="votre série")
    
    nationality=models.CharField(null=True,max_length=100,verbose_name="nationnalité")
    
    email = models.EmailField(max_length=100,null=True)
    baccmark=models.IntegerField(default=10,verbose_name="moyenne générale au bacc")
    probatoiremark=models.IntegerField(default=10,verbose_name="moyenne générale au probatoire")
    phone = models.CharField(max_length=100,null=True,verbose_name="téléphone")
    region=models.CharField(max_length=100,null=True)
    adresse=models.CharField(max_length=100,null=True)
    cni_number = models.PositiveBigIntegerField(null=True,verbose_name="numéro de cni")
    
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
    
    def save(self, *args, **kwargs):
        tournament_candidacy=Candidacy.objects.filter(tournament=self.tournament)
        if(tournament_candidacy.count()>0):
            last=tournament_candidacy.last()
            number=last.anonymat_number[1:]
            value=int(number)+1
            self.anonymat_number='A'+str(value).zfill(5)
            
        else:
            self.anonymat_number="A00000"
        
        super().save(*args, **kwargs)
    
    def __str__(self):
        return  self.name+' ' + self.lastname + ' :' + str(self.cni_number)
    
        
class OralNote(models.Model):
    candidate=models.ForeignKey(Candidacy,on_delete=models.CASCADE,null=True)
    note=models.IntegerField(default=10)
    observation=models.TextField(null=True,blank=True)




class WritingNote(models.Model):
    matiere=models.ForeignKey(TournamentSubject,on_delete=models.deletion.PROTECT,null=True)
    candidate=models.ForeignKey(Candidacy,on_delete=models.CASCADE)
    note=models.IntegerField(default=10)

    


    
    
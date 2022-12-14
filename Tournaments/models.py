from django.db import models

# Create your models here.

class Tournament(models.Model):
    titre=models.CharField(max_length=100)
    description=models.TextField(null=True)
    date_annonce=models.DateTimeField(auto_now_add=True)
    date_lancement=models.DateTimeField(null=True)
    

class OralSession(models.Model):
    date=models.DateField();
    tournament=models.models.ForeignKey(Tournament, verbose_name=_(""), on_delete=models.CASCADE)

class WritingSession(models.Model):
    date=models.DateField();
    tournament=models.ForeignKey(Tournament, verbose_name=_(""), on_delete=models.CASCADE)
    


    
    
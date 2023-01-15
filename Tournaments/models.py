from django.db import models
from django.utils.translation import gettext_lazy as _
# Create your models here.

class Tournament(models.Model):
    YEAR_IN_SCHOOL_CHOICES = [
        ('cl1i', 'Concours licence I informatique'),
        ('cl1m', 'Concours licence I Management'),
        ('cing1i', 'Concours ingenieur I informatique'),
        ('cing3i', 'Coucours ingenieur III informatique'),
        ('cm1m', 'Concours Master I Management'),
        ('cm1i', 'Concours Master I informatique '),
    ]

    type = models.CharField(
        max_length=7,
        choices=YEAR_IN_SCHOOL_CHOICES,
        default="S0",
    )    

    description=models.TextField(null=True)
    date_annonce=models.DateTimeField(auto_now_add=True)
    date_inscription=models.DateTimeField(null=True)

    nbr_place=models.IntegerField(default=300)    

class OralSession(models.Model):
    date=models.DateField(null=True);
    tournament=models.ForeignKey(Tournament, verbose_name=(""), on_delete=models.CASCADE)

class WritingSession(models.Model):
    date=models.DateField(null=True);
    tournament=models.OneToOneField(Tournament, verbose_name=(""), on_delete=models.CASCADE)
    


    
    
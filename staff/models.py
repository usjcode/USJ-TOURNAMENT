
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _
from django.contrib.auth import get_user_model


class EmailUser(AbstractUser):
    email = models.EmailField(_('email address'), unique=True)

class Staff(models.Model):
    ROLE_CHOICE=[("S","sécretaire"),
                 ("D","directeur"),
                 ("RCL1I","responsable de concours licence informatique"),
                 ("RCM1I","responsable de concours master 1 informatique"),
                 ("RCINGI","responsable de concours ingenieur informatique")
                 ]
    avatar=models.ImageField(null=True)
    name = models.CharField(max_length=100, blank=True, null=True)
    role=models.CharField(max_length=50,choices=ROLE_CHOICE)
    bio=models.TextField(default="do you know ngdream likes banana ???")
    user=models.OneToOneField(EmailUser,  on_delete=models.CASCADE,null=True)
    
    
class StaffInvitation(models.Model):
    ROLE_CHOICE=[("S","sécretaire"),
                ("D","directeur"),
                ("RCL1I","responsable de concours licence informatique"),
                ("RCM1I","responsable de concours master 1 informatique"),
                ("RCINGI","responsable de concours ingenieur informatique")
                ]
    email= models.EmailField(null=True)
    send_date= models.DateField("", auto_now_add=True)
    role=models.CharField(max_length=100, null=True,choices=ROLE_CHOICE)
    note=models.TextField(null=True)
    
    def __str__(self) -> str:
        return self.email + " " + self.role
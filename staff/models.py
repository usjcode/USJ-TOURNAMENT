
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _


class EmailUser(AbstractUser):
    email = models.EmailField(_('email address'), unique=True)

class staff(models.Model):
    avatar=models.ImageField(null=True)
    role=models.CharField("invité", max_length=50)
    bio=models.TextField(null=True)
    
    
    
from django.db import models

# Create your models here.


from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _


class EmailUser(AbstractUser):
    email = models.EmailField(_('email address'), unique=True)

class staff(models.Model):
    role=models.models.CharField("invité", max_length=50)
    
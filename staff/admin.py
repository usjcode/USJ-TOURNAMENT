from django.contrib import admin
from .models import StaffInvitation,EmailUser
# Register your models here.

admin.site.register(StaffInvitation)
admin.site.register(EmailUser)
from django.contrib import admin
from .models import Staff,StaffInvitation,EmailUser
# Register your models here.

admin.site.register(Staff)
admin.site.register(StaffInvitation)
admin.site.register(EmailUser)
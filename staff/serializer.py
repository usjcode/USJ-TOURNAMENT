from rest_framework import serializers

from .models import StaffInvitation

class StaffSerializer(serializers.ModelSerializer):
    class Meta:
        model = StaffInvitation
        fields = ('email', 'role')
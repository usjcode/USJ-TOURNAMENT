from django import  forms
from .models import StaffInvitation



from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import get_user_model
from django import forms


# form for add staff member
class AddStaffForm(forms.Form):
    class Meta:
        model = StaffInvitation
        fields = ('email', 'role')

# login form
class LoginForm(AuthenticationForm):
    username = forms.CharField(label='Email or Username')
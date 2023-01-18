from django import  forms
from .models import StaffInvitation

from django.contrib.auth.forms import UserCreationForm, AuthenticationForm,SetPasswordForm
from .models import EmailUser
from django import forms
from django.contrib.auth import get_user_model



class Passwordform(SetPasswordForm):
    class Meta:
        model = get_user_model()
        fields = ['new_password1', 'new_password2']
# form for add staff member
class AddStaffForm(forms.ModelForm):
    class Meta:
        model = StaffInvitation
        fields = ('email', 'role')

# login form
class LoginForm(AuthenticationForm):
    username = forms.CharField(label='Email or Username')
    

class EditUserForm(forms.ModelForm):
    class Meta:
        model = EmailUser
        fields=('avatar','name',"contact","email","bio")
        widgets={
            "avatar":forms.FileInput(attrs={'class':'form-control'}),
            "email":forms.EmailInput(attrs={'class':'form-control'}),
            "name":forms.TextInput(attrs={'class':'form-control'}),
            "bio":forms.Textarea(attrs={'class':'form-control'}),
            "contact":forms.TextInput(attrs={'class':'form-control','type':'number'}),
            }
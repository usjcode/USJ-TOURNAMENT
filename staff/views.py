from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import View
from django.views.generic.edit import FormView,UpdateView
from django.contrib.auth import logout,authenticate,login
from django.contrib.auth.models import User
from django.shortcuts import redirect ,render
from .forms import AddStaffForm,LoginForm,EditUserForm,Passwordform
from django.core.mail import EmailMessage
from .models import StaffInvitation,EmailUser
from django.core.mail import send_mail
from django.contrib.auth import update_session_auth_hash

import random
import string


##################
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.http import JsonResponse
from .serializer import StaffSerializer
from rest_framework import generics


################## create
class CreateStaffView(generics.CreateAPIView):
    queryset = StaffInvitation.objects.all()
    serializer_class = StaffSerializer
    def perform_create(self, serializer):
        email = serializer.validated_data.get('email')
        role = serializer.validated_data.get('role') or None
        if role is None:
            role = 'D'
        serializer.save(role = role)

################## end
class DetailStaffView(generics.RetrieveAPIView):
    queryset = StaffInvitation.objects.all()
    serializer_class = StaffSerializer

#################

def get_random_string(length):
    # choose from all lowercase letter
    letters = string.ascii_lowercase
    result_str = ''.join(random.choice(letters) for i in range(length))
    return result_str

def change_password(request):
    if request.method == 'POST':
        form = Passwordform(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)
            return redirect('staff')
    else:
        form = Passwordform(request.user)
    return render(request, 'change-password.html', {
        'form': form
    })

class EditView(UpdateView,LoginRequiredMixin):
    template_name = 'edit_staff.html'
    form_class = EditUserForm
    success_url="/staff"
    model=EmailUser
    def form_valid(self, form):
        form.save()
        return super().form_valid(form)

def staffremove(request,id):
    staff=EmailUser.objects.get(id=id)
    send_mail("alerte suppression de compte",
            'votre compte à été supprimer par un administrateur',
            'TON ADDRESSE MAIL',
            [staff.email],
            fail_silently=False)
    staff.delete()
    return redirect("staff")
    
# staff's view
class StaffView(LoginRequiredMixin,TemplateView):
    template_name = 'staff.html'
    def get_context_data(self, **kwargs):
        context=super().get_context_data(**kwargs)
        context["staffs"]=EmailUser.objects.all()
        return context
    
    
# login page
class LoginView(FormView):
    template_name = 'login.html'
    form_class = LoginForm
    success_url="/"
    def form_valid(self, form):
        username=self.request.POST["username"]
        password=self.request.POST["password"]
        print(username,password)
        user = authenticate(username=username,password=password)
        login(self.request,user)
        if next in self.request.GET.keys():
            return redirect(self.request.GET["next"])
        return super().form_valid(form)


class LogoutView(View):
    def get(self,request,*args,**kwargs):
        logout(request)
        return redirect("home")
        

class StaffProfilView(LoginRequiredMixin,TemplateView):
    template_name = 'profil.html'
    def get_context_data(self, **kwargs):
        id=kwargs["id"]
        context=super().get_context_data(**kwargs)
        staff=EmailUser.objects.get(id=id)
        context["staff"]=staff
        
        return context
    

# la vue pour les invitation
class InvitationView(LoginRequiredMixin,TemplateView):
    template_name = 'invitation.html'
    def get_context_data(self,**kwargs):
        id=kwargs["id"]
        invitation=StaffInvitation.objects.get(id=id)
        randompassword=get_random_string(8)
        username=invitation.email
        name="utilisateur"+str(invitation.id)
        
        newuser:EmailUser
        if invitation.active:
        
            newuser=EmailUser(username=username,email=invitation.email,role=invitation.role,name=name)
            newuser.set_password(randompassword)
            newuser.save()     
            invitation.active=False
            invitation.save()
            
            
            
        
        context={
            "password":randompassword,
            "username":username,
            "email":invitation.email,
            "request":self.request
        }
        
        
        return context





    
class AddView(LoginRequiredMixin,FormView):
    template_name = 'add_staff.html'
    form_class = AddStaffForm
    success_url="/staff"

    def form_valid(self, form):
        inv = form.save()      
        mail_send = inv.email
        id_send = inv.id
                
        send_mail("INVITATION POUR L'UTILISATION DU LOGICIEL DE GESTION DE CONCOURS DE USJ",
            'Veuiller cliquez ici pour active votre compte utilisateur 127.0.0.1:8000/staff/invitation/{}'.format(id_send),
            'TON ADDRESSE MAIL',
            [mail_send],
            fail_silently=False
        )
          
        return super().form_valid(form)

    
    

from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.http import JsonResponse
from api.serializer import MyTokenObtainPairSerializer, RegisterSerializer
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework import generics
from django.contrib.auth.models import User
from rest_framework.permissions import AllowAny, IsAuthenticated

# Create your views here.

class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer

class RegisterView(generics.CreateAPIView):
    queryset = EmailUser.objects.all()
    permission_classes = (AllowAny,)
    serializer_class = RegisterSerializer


@api_view(['GET'])
def getRoutes(request):
    routes = [
        '/api/token/',
        '/api/register/',
        '/api/token/refresh/'
    ]
    return Response(routes)
from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import View
from django.views.generic.edit import FormView
from django.contrib.auth import logout,authenticate,login
from django.shortcuts import redirect
from .forms import AddStaffForm,LoginForm
from django.core.mail import EmailMessage
from .models import Staff ,StaffInvitation,EmailUser



# staff's view
class StaffView(LoginRequiredMixin,TemplateView):
    template_name = 'staff.html'
    def get_context_data(self, **kwargs):
        context=super().get_context_data(**kwargs)
        context["staffs"]=Staff.objects.all()
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
        staff=Staff.objects.get(id=id)
        context["staff"]=staff
        
        return context
    

class InvitationView(TemplateView):
    template_name = 'invitation.html'
    def get_context_data(self,**kwargs):
        id=kwargs["id"]
        invitation=StaffInvitation.objects.get(id=id)
        randompassword="ccccc"
        username="banana"
        newuser:EmailUser
        if invitation.active:
        
            newuser=EmailUser(username=username,email=invitation.email)
            newuser.set_password(randompassword)
            newuser.save()
            Staff.objects.create(name=username,role=invitation.role,user=newuser)
            
            invitation.active=False
            invitation.save()
            
        
        context={
            "password":randompassword,
            "username":username,
            "email":invitation.email
        }
        
        return context

    
class AddView(LoginRequiredMixin,FormView):
    template_name = 'add_staff.html'
    form_class = AddStaffForm
    success_url="/staff"

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)
    
    



from django.shortcuts import render
from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import View
from django.views.generic.edit import FormView
from django.contrib.auth import logout,views
from django.shortcuts import redirect
from .forms import AddStaffForm,LoginForm

from .models import Staff
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login



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
    


    



class AddView(LoginRequiredMixin,FormView):
    template_name = 'add_tournament.html'
    form_class = AddStaffForm

    def form_valid(self, form):
        # This method is called when valid form data has been POSTed.
        # It should return an HttpResponse.
        form.send_email()
        return super().form_valid(form)


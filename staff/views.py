from django.shortcuts import render
from django.views.generic import TemplateView
from django.views.generic.edit import FormView
from .forms import AddStaffForm
# Create your views here.

def login_view(request):
    return render(request,"login.html")




class StaffView(TemplateView):
    template_name = 'staff.html'
    
class LoginView(TemplateView):
    template_name = 'staff.html'
    
class LogoutView(TemplateView):
        template_name = 'staff.html'
    

class StaffProfilView(TemplateView):
    template_name = 'profil.html'


    



class AddView(FormView):
    template_name = 'add_tournament.html'
    form_class = AddStaffForm

    def form_valid(self, form):
        # This method is called when valid form data has been POSTed.
        # It should return an HttpResponse.
        form.send_email()
        return super().form_valid(form)


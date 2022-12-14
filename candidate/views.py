from django.shortcuts import render
<<<<<<< HEAD

# Create your views here.
=======
from .models import Tournament
from django.views.generic import TemplateView
from django.views import View
from django.views.generic.edit import FormView
# Create your views here.




# some_app/views.py


class AboutView(TemplateView):
    template_name = "about.html"
    
    

class HomeView(View):
    template_name = 'form_template.html'
    def get(self, request, *args, **kwargs):
        return  render(request,self.template_name)
    



class AddView(FormView):
    template_name = 'add_tournament.html'
    form_class = AddTournamentForm

    def form_valid(self, form):
        # This method is called when valid form data has been POSTed.
        # It should return an HttpResponse.
        form.send_email()
        return super().form_valid(form)

>>>>>>> 24d2046 (is comming)

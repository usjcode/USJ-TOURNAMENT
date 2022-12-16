from django.shortcuts import render
from .models import Tournament
from django.views.generic import TemplateView
from django.views import View
from django.views.generic.edit import FormView

from .forms import AddTournamentForm
# Create your views here.




# some_app/views.py


class AboutView(TemplateView):
    template_name = "about.html"
    
    

class HomeView(TemplateView):
    template_name = 'home.html'
    def get_context_data(self, **kwargs):
        context=super().get_context_data(**kwargs)
        context["tournaments"]=Tournament.objects.all()
        return context


class TournamentView(TemplateView):
    template_name = 'tournament.html'
    def get_context_data(self, **kwargs):
        context=super().get_context_data(**kwargs)
        return context
    



class AddView(FormView):
    template_name = 'add_tournament.html'
    form_class = AddTournamentForm

    def form_valid(self, form):
        # This method is called when valid form data has been POSTed.
        # It should return an HttpResponse.
        form.send_email()
        return super().form_valid(form)


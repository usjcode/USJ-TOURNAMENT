from django.shortcuts import render,redirect
from .models import Tournament
from django.views.generic import TemplateView
from django.views import View
from django.views.generic.edit import FormView,UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin

from .forms import AddTournamentForm



# Create your views here.




# some_app/views.py


class AboutView(TemplateView):
    template_name = "about.html"
    
    

class HomeView(LoginRequiredMixin,TemplateView):
    template_name = 'home.html'
    def get_context_data(self, **kwargs):
        context=super().get_context_data(**kwargs)
        context["tournaments"]=Tournament.objects.all()
        return context


class TournamentView(LoginRequiredMixin,TemplateView):
    template_name = 'tournament.html'
    def get_context_data(self, **kwargs):
        id=kwargs.get('id')
        
        context=super().get_context_data(**kwargs)
        context['tournament']=Tournament.objects.get(id=id)
        return context
    



class AddView(LoginRequiredMixin,FormView):
    success_url="/"
    template_name = 'add_tournament.html'
    form_class = AddTournamentForm

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)
    


class Updateview(UpdateView):
    template_name = 'add_candidate.html'
    model = Tournament
    form_class = AddTournamentForm
    success_url='/tournament'


def deleteview(request,id):
    Tournament=Tournament.objects.get(id=id)
    Tournament.delete()
    return redirect("tournament")

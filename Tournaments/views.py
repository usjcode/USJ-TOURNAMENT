from django.shortcuts import render,redirect
from .models import Tournament
from candidate.models import Candidacy
from django.views.generic import TemplateView
from django.views import View
from django.views.generic.edit import FormView,UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models.functions import Now
import datetime

from .forms import AddTournamentForm,UpdateTournamentForm



class AboutView(TemplateView):
    template_name = "about.html"
    
    

class HomeView(LoginRequiredMixin,TemplateView):
    template_name = 'home.html'
    def get_context_data(self, **kwargs):
        context=super().get_context_data(**kwargs)
        context["tournaments"]=Tournament.objects.all().reverse()
        return context


class TournamentView(LoginRequiredMixin,TemplateView):
    template_name = 'tournament.html'
    def get_context_data(self, **kwargs):
        id=kwargs.get('id')
        context=super().get_context_data(**kwargs)
        tournament=Tournament.objects.get(id=id)
        context['tournament']=tournament
        context['candidats']=Candidacy.objects.filter(tournament=context['tournament'])
        context['c'] =0
        if datetime.date.today() >=tournament.date_debut:
            context['c'] =1
        return context
    



class AddView(LoginRequiredMixin,FormView):
    success_url="/"
    template_name = 'add_tournament.html'
    form_class = AddTournamentForm

    def form_valid(self, form):
        
        form.save()
        return super().form_valid(form)
    


class Updateview(UpdateView):
    template_name = 'add_tournament.html'
    model = Tournament
    form_class = UpdateTournamentForm
    success_url='/'


def deleteview(request,id):
    tournament=Tournament.objects.get(id=id)
    candidates=Candidacy.objects.filter(tournament=tournament)
    candidates.delete()
    tournament.delete()
    return redirect("home")

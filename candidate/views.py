from django.shortcuts import render,redirect
from .models import Tournament,Candidacy
from django.views.generic import TemplateView
from django.views import View
from django.views.generic.edit import FormView,UpdateView
from .forms import AddCandidateForm
from django.db.models.functions import Now
from django.contrib.auth.mixins import LoginRequiredMixin
import datetime
# Create your views here.


class HomeView(LoginRequiredMixin,View):
    template_name = 'candidates.html'
    def get(self, request, *args, **kwargs):
        candidats=Candidacy.objects.all()
        context={}
        if("search" in self.request.GET.keys()):
            search=self.request.GET.get("search")
            context["searched"]=search
            candidats=Candidacy.objects.filter(cni_number=search)
        context["candidats"]=candidats
        return  render(request,self.template_name,context=context)
    
def deleteview(request,id):
    candidate=Candidacy.objects.get(id=id)
    candidate.delete()
    return redirect("candidate")



class AddView(FormView):
    template_name = 'add_candidate.html'
    form_class = AddCandidateForm
    success_url='/'

    def form_valid(self, form):
        candidat=form.save(commit=False)
        type=self.kwargs["tournament"]
        print(type)
        tournament=Tournament.objects.filter(date_inscription__gt=Now(),type=type).first()
        candidat.tournament=tournament
        candidat.save()
        return super().form_valid(form)
    
    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        # Add in a QuerySet of all the books
        print(self.kwargs["tournament"])
        context['c'] = Tournament.objects.filter(date_inscription__gt=Now(),type=self.kwargs["tournament"]).exists()
        context['type']=self.kwargs["tournament"]
        print(context['c'])
        return context


class Updateview(UpdateView):
    template_name = 'update_candidate.html'
    model = Candidacy
    form_class = AddCandidateForm
    success_url='/candidate'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        id=self.kwargs['pk']
        candidate=Candidacy.objects.get(pk=id)
        context['c'] =True
        if datetime.date.today() >=candidate.tournament.date_debut:
            context['c'] =False
        return context
    
    

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)


class Updatetournamentview(LoginRequiredMixin,View):
        def get(self, request, *args, **kwargs):
            id=kwargs["pk"]
            tournamentname=kwargs["tournament"]
            candidat=Candidacy.objects.get(id=id)
            exist=Tournament.objects.filter(date_inscription__gt=Now(),type=tournamentname).exists()
            success=False
            if exist:
                tournament=Tournament.objects.filter(date_inscription__gt=Now(),type=tournamentname).first()
                candidat.tournament=tournament
                candidat.save()
                success=True
                return redirect("candidate")
                
            return  render(request,"updatecandidatetournament.html",context={"success":success})

    
    
    
    




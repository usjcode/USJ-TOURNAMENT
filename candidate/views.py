from django.shortcuts import render,redirect
from .models import Tournament,Candidacy
from django.views.generic import TemplateView
from django.views import View
from django.views.generic.edit import FormView,UpdateView
from .forms import AddCandidateForm
from django.db.models.functions import Now
from django.contrib.auth.mixins import LoginRequiredMixin
# Create your views here.


class AboutView(TemplateView):
    template_name = "about.html"
    
    

class HomeView(LoginRequiredMixin,View):
    template_name = 'candidates.html'
    def get(self, request, *args, **kwargs):
    
        context={"candidats":Candidacy.objects.all()}
        return  render(request,self.template_name,context=context)
    
def deleteview(request,id):
    candidate=Candidacy.objects.get(id=id)
    candidate.delete()
    return redirect("candidate")

#view for add candidate
class ChoiseAddView(LoginRequiredMixin,FormView):
    template_name = 'add_candidate.html'
    form_class = AddCandidateForm
    def form_valid(self, form):
        pass

class AddView(FormView):
    template_name = 'add_candidate.html'
    form_class = AddCandidateForm
    success_url='/'

    def form_valid(self, form):
        candidat=form.save(commit=False)
        type=self.kwargs["tournament"]
        tournament=Tournament.objects.filter(date_inscription__gt=Now(),type=type).first()
        candidat.tournament=tournament
        candidat.save()
        
        tournament.nbr_place-=1
        tournament.save()
        return super().form_valid(form)
    
    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        # Add in a QuerySet of all the books
        print(self.kwargs["tournament"])
        context['c'] = Tournament.objects.filter(date_inscription__gt=Now(),type=self.kwargs["tournament"]).exists()
        
        return context


class Updateview(UpdateView):
    template_name = 'add_candidate.html'
    model = Candidacy
    form_class = AddCandidateForm
    success_url='/candidate'
    
    

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)
    




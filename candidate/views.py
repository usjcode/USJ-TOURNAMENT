from django.shortcuts import render
from .models import Tournament
from django.views.generic import TemplateView
from django.views import View
from django.views.generic.edit import FormView
from .forms import AddCandidateForm
from django.db.models.functions import Now
from django.contrib.auth.mixins import LoginRequiredMixin
# Create your views here.


class AboutView(TemplateView):
    template_name = "about.html"
    
    

class HomeView(LoginRequiredMixin,View):
    template_name = 'candidates.html'
    def get(self, request, *args, **kwargs):
        
        return  render(request,self.template_name)
    


#view for add candidate
class AddView(FormView):
    template_name = 'add_candidate.html'
    form_class = AddCandidateForm
    def form_valid(self, form):
        form.save()

class AddCCL1IView(FormView):
    template_name = 'add_candidate.html'
    form_class = AddCandidateForm
    success_url='/'

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)
    
    
    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        # Add in a QuerySet of all the books
        context['cl1'] = Tournament.objects.filter(date_inscription__gt=Now(),type='cl1i')
        return context



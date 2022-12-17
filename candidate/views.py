from django.shortcuts import render
from .models import Tournament
from django.views.generic import TemplateView
from django.views import View
from django.views.generic.edit import FormView
from .forms import AddCandidateForm
from django.contrib.auth.mixins import LoginRequiredMixin
# Create your views here.


class AboutView(TemplateView):
    template_name = "about.html"
    
    

class HomeView(LoginRequiredMixin,View):
    template_name = 'form_template.html'
    def get(self, request, *args, **kwargs):
        return  render(request,self.template_name)
    


#view for add candidate
class AddView(FormView):
    template_name = 'add_candidate.html'
    form_class = AddCandidateForm

    def form_valid(self, form):
        # This method is called when valid form data has been POSTed.
        # It should return an HttpResponse.
        form.send_email()
        return super().form_valid(form)



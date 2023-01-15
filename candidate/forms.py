from .models import Candidacy
from django import  forms


class AddCandidateForm(forms.ModelForm):
    class Meta:
        model=Candidacy
        exclude=('tournament','anonymat_number=')
        widgets={"bacc":forms.CheckboxInput(attrs={"class": "form-check-input"}),
       "hasrepeated":forms.CheckboxInput(attrs={"class": "form-check-input"}),
       "birth_date":forms.widgets.DateInput(attrs={'type': 'date'})}
    

from django import forms
from .models import job
  
class jobForm(forms.ModelForm):
    class Meta:
        model = job
        fields = ['title', 'Company_name', 'salary']
        

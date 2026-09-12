from django.shortcuts import render , redirect 
from .models import CustomCreationForm
# Create your views here.
def signup(request):
    if request.method == 'POST':
       form = CustomCreationForm(request.POST)
       if form.is_valid():
           form.save()
           return redirect('/login')
       
    else:
        form = CustomCreationForm()
    return render(request, 'C:\Users\MEGHNA SINGH\Desktop\JOB_PORTAL\jobportal\accounts\templates\signup.html')
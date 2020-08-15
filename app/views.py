from django.shortcuts import render
from django.views.generic import TemplateView

# Create your views here.
def home(request):
    context = {}

    return render(request, 'pages/home.html', context=context)

 

from django.shortcuts import render
from .models import Carrier

def home(request):
    carriers = Carrier.objects.all()
    context = {
        'carriers': carriers,
        'phone': "8375074624",
        'insta': "shipworld_curier",
        'owner': "Chaten Gupta"
    }
    # Update the line below to just 'index.html'
    return render(request, 'index.html', context)
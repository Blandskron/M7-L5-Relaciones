from django.shortcuts import render
from .models import Region

def index(request):
    context = {
        "regiones": Region.objects.all()
    }
    return render(request, 'muchos_a_uno/index.html', context)

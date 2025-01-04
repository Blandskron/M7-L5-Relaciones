from django.shortcuts import render
from .models import Trabajador

def index(request):
    context = {
        "trabajadores": Trabajador.objects.all()
    }
    return render(request, 'uno_a_uno/index.html', context)

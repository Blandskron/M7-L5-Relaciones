from django.shortcuts import render
from .models import Cliente

def index(request):
    context = {
        "clientes": Cliente.objects.all()
    }
    return render(request, 'muchos_a_muchos/index.html', context)

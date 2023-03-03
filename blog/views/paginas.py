from django.contrib.auth.decorators import login_required
from django.shortcuts import render

def index(request):
    return render(request, 'index.html', {})
def sobre(request):
    return render(request, 'sobre.html', {})

def curso(request):
    return render(request, 'curso.html')

@login_required
def secretario(request):
    return render(request, 'secretario.html')
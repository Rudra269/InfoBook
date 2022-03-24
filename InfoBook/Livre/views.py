from django.shortcuts import render
from .models import Livre

def index(request):
    livre = Livre.objects.all()
    return render(request, 'index.html', {'Livre':Livre})

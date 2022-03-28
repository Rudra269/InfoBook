from django.shortcuts import render,get_object_or_404
from .models import Genre
from Livre.models import Livre

def index(request):
    genre = Genre.objects.all()
    return render(request,'index.html',{'genre':genre})

def genre1(request):
    livre2 = Livre.objects.all()

    return render(request,f"genre1.html",{'livre':livre2})

def genre2(request):
    livre2 = Livre.objects.all()

    return render(request,f"genre2.html",{'livre':livre2})

# Create your views here.

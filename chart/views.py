from django.shortcuts import render
from .models import *
# Create your views here.
def index (request):
    ur = people.objects.all().order_by('-id')
    return render(request,'chart/index.html',{'ur': ur})
    
def detail (request,key):
    ab = people.objects.get(name=key)
    return render(request,'chart/detail.html',{'ab': ab})
    
    
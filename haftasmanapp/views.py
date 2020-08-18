from django.shortcuts import render
from django.shortcuts import HttpResponse

# Create your views here.
# def home(repuest):
    # pass

def home(request):
    return render(request,'haftasmanapp/home.html')


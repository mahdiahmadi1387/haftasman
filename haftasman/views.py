from django.shortcuts import render
from django.shortcuts import HttpResponse


def home (repuest):
    return render(repuest,'templates/home.html')

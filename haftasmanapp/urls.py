from django.urls import path, include
from . import views

app_name = 'hatfasmanapp'

urlpatterns = [
    path('',views.home),
    
]
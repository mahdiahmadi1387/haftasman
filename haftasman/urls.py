from django.contrib import admin
from django.urls import path, include
from . import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns


urlpatterns = [
    path('admin/', admin.site.urls),
    # path('',views.home),
    # path('haftasmanapp/',include('haftasmanapp.urls'))
    path('',include('haftasmanapp.urls')),

]

urlpatterns += staticfiles_urlpatterns()



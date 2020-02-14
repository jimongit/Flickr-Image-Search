from django.contrib import admin
from django.urls import path, include
from imagesearch import views

urlpatterns = [    
    path('', include('imagesearch.urls')),
    path('users/', include('users.urls')),
    path('users/', include('django.contrib.auth.urls')),   
    path('admin/', admin.site.urls),
] 

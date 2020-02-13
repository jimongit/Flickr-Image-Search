from django.urls import path
from . import views

urlpatterns = [
      path('', views.home, name='home'),
      path('search_results/', views.search_result, name='search_results'),
      path('ajax/', views.ajax, name='ajax'),
]

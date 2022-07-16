from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name = "home"),
    path('about/', views.about, name = "about"),
    path('projects/', views.projects, name = "projects"),

    path('home/', views.home2, name = "home2"),
    
    path('home3/', views.home3, name = "home3"),

]
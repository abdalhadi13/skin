
from django.urls import path,include 
from . import views
urlpatterns = [
    path('form',views.testfun),
    path('home',views.justfun),
    path('index',views.havefun)
]   

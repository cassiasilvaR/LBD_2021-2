from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index') #Vai direcionar para a página principal
]
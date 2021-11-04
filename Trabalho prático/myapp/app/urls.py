from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'), #Vai direcionar para a página principal
    path('counter', views.counter, name='counter') #Um dos parametros é o nome da função
]
"""project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from app.views import form_e, home, form, create, view, edit, update, form_e, update_e, create_e, emprestar, create_user, form_user

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'), 
    path('form/', form, name='form'),
    path('form_e/', form_e, name= 'form_e'),
    path('create_e/', create_e, name='create_e'),
    path('create/', create, name='create'),
    path('view/<int:pk>/', view, name='view'),  
    path('edit/<int:pk>/', edit, name='edit'),
    path('update_e/<int:pk>/', update_e, name = 'uptade_e'),
    path('update/<int:pk>/', update, name='update'),
    path('emprestar/<int:pk>/', emprestar, name='emprestar'),
    path('form_user/', form_user, name='form_user'),
    path('create_user/', create_user, name='create_user')
]

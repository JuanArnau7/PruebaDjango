"""Proyecto1 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from Proyecto1.views import cuando_naci
from Proyecto1.views import saludo, chau, hoy, saludar_a, ejemplo_template

urlpatterns = [
    path('admin/', admin.site.urls),
    path('hola/', saludo),
    path('chau/', chau),
    path('hoy/', hoy),
    path('minombre/<nombre>', saludar_a),
    path('template/', ejemplo_template),
    path('cuando_naci/<edad>', cuando_naci)
]

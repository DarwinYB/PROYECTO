"""Proyecto3A URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from core import views

urlpatterns = [
    path('', views.home, name="home"),
    path('empleados/', views.empleados, name="empleados"),
    path('horario/', views.horario, name="horario"),
    path('modificacion/', views.modificacion, name="modificacion"),
    path('asistencia/', views.asistencia, name="asistencia"),
    path('modificaciona/', views.modificaciona, name="modificaciona"),
    path('registro_docente/', views.registro_docente, name="registro_docente"),
    path('reporte/', views.reporte, name="reporte"),
    path('vacaciones/', views.vacaciones, name="vacaciones"),
    path('admin/', admin.site.urls),

]


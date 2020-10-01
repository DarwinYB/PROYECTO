from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from .models import Horario, Asistencia, Vacaciones, Reportes, Semana


class AsistenciaForm(forms.ModelForm):
    class Meta:
        model = Asistencia  #relacionar el archivo de modelo
        fields = ['nombre', 'apellido', 'jornada']  #ingreso o salida de campos


class HorariosForm(forms.ModelForm):
    class Meta:
        model = Horario
        fields = ['dias',  'Hora_entrada', 'Hora_Salida']


class VacacionesForm(forms.ModelForm):
    class Meta:
        model = Vacaciones
        fields = ['Nombre', 'Apellido', 'Fecha_Inicio', 'Fecha_Culminacion']


class ReportesForm(forms.ModelForm):
    class Meta:
        model = Reportes
        fields = ['Fecha_Reporte', 'Ced_Empleado', 'Nombre', 'Apellido', 'Area']


class DiasForm(forms.ModelForm):
    class Meta:
        model = Semana
        fields = ['dias']
# Create your views here.
from django.contrib.auth import login, authenticate, logout
from django.shortcuts import render, HttpResponse, redirect, get_object_or_404
from .forms import AsistenciaForm, HorariosForm, VacacionesForm, ReportesForm, DiasForm
from .models import Horario, Semana
# Create your views here.
from django.contrib.auth.decorators import login_required


@login_required(None, "", 'login')
def home(request, plantilla ="home.html"):
    if request.user.is_authenticated:
        return render(request, plantilla)
        # En otro caso redireccionamos al login
    return redirect('login')


def reporte(request, plantilla="reporte.html"):
    return render(request, plantilla);


def vacaciones(request, plantilla="vacaciones.html"):
    return render(request, plantilla);


def asistencia(request, plantilla="asistencia.html"):
    if request.method == 'POST':
        asistenciasForm = AsistenciaForm(request.POST)
        if asistenciasForm.is_valid():
            asistenciasForm.save()
            return redirect("asistecias")
        else:
            asistenciasForm = AsistenciaForm()
        return render(request, plantilla, {'form': AsistenciaForm})
    return render(request, 'asistencia.html')


def vacaciones(request, plantilla="vacaciones.html"):
    if request.method == 'POST':
        vacacionesForm = VacacionesForm(request.POST)
        if vacacionesForm.is_valid():
            vacacionesForm.save()
            return redirect("vacaciones")
        else:
            vacacionesForm = VacacionesForm()
        return render(request, plantilla, {'form': VacacionesForm})
    return render(request, 'vacaciones.html')


def reporte(request, plantilla="reporte.html"):
    if request.method == 'POST':
        reporteForm = ReportesForm(request.POST)
        if reporteForm.is_valid():
            reporteForm.save()
            return redirect("reporte")
        else:
            reporteForm = ReportesForm()
        return render(request, plantilla, {'reporteform': reporteForm})
    return render(request, 'reporte.html')


@login_required(None, "", 'login')
def crearhorario(request, plantilla="horario/crearhorario.html"):
    if request.method == 'POST':
        horarioForm = HorariosForm(request.POST)
        if horarioForm.is_valid():
            horarioForm.save()
            return redirect("horario")
    else:
        horarioForm = HorariosForm()
    return render(request, plantilla, {'horarioform': horarioForm})


@login_required(None, "", 'login')
def horario(request, plantilla="horario/horario.html"):
    horarios = list(Horario.objects.all())
    return render(request, plantilla, {'horarios': horarios})


@login_required(None, "", 'login')
def horariomod(request, pk, plantilla="horario/horariomod.html"):
    if request.method == "POST":
        horario = get_object_or_404(Horario, pk=pk)
        horarioform = HorariosForm(request.POST or None, instance=horario)
        if horarioform.is_valid():
            horarioform.save()
        return redirect("horario")
    else:
        horario= get_object_or_404(Horario, pk=pk)
        horarioform = HorariosForm(request.POST or None, instance=horario)
        return render(request, plantilla, {'horarioform': horarioform})


@login_required(None, "", 'login')
def horarioelim(request, pk,  plantilla="horario/horarioelim.html"):
    if request.method == "POST":
        horario = get_object_or_404(Horario, pk=pk)
        horarioForm = HorariosForm(request.POST or None, instance=horario)
        if horarioForm.is_valid():
            horario.delete()
        return redirect("horario")
    else:
        horario = get_object_or_404(Horario, pk=pk)
        horarioForm = HorariosForm(request.POST or None, instance=horario)
    return render(request, plantilla, {'horarioForm': horarioForm})


def dias(request, plantilla="Dia.html"):
    if request.method == 'POST':
        dia = DiasForm(request.POST)
        if dia.is_valid():
            dia.save()
            return redirect(dias)
    else:
        dia = DiasForm()
    return render(request, plantilla, {'formulario': dia})


def dias(request, plantilla="Dia.html"):
    dias = list(Semana.objects.all())
    return render(request, plantilla, {'dias': dias})

# Create your views here.
from django.shortcuts import render
from django.shortcuts import render, HttpResponse

# Create your views here.


html_base = """
    <h1>Mi Primer Menu</h1>
     <ul>
        <li>   <a href="/">Ingreso al Sistema</a>              </li>
        <li>   <a href="/empleados/">Ingreso de empleados</a>   </li>
        <li>   <a href="/horario/">Ingreso de horario</a>     </li>
        <li>   <a href="/modificacion/">Modificacion de horario</a>     </li>
        <li>   <a href="/asistencia/">Ingreso de Asistencia</a>     </li>

    </ul>
"""


def home(request):
    html_response = "<h1>Mi sistema</h1>"
    for i in range(10):
        html_response += "<h2>Portada</h2>"
    return HttpResponse(html_response);


# relaciona la parte vista con el template home.html


def home(request):
    html_responsde = "<h1>la pagina de ingreso al sistema</h1>"
    html_responsde = html_base + html_responsde
    return HttpResponse(html_responsde);


def empleado(request):
    html_responsde = "<h1>EMPLEADOS </h1>"
    html_responsde = html_base + html_responsde
    return HttpResponse(html_responsde);


def horario(request):
    html_responsde = "<h1>HORARIO</h1>"
    html_responsde = html_base + html_responsde
    return HttpResponse(html_responsde);


def modificacion(request):
    html_responsde = "<h1>Modificacion</h1>"
    html_responsde = html_base + html_responsde
    return HttpResponse(html_responsde);


def asistencia(request):
    html_responsde = "<h1>Asistencia</h1>"
    html_responsde = html_base + html_responsde
    return HttpResponse(html_responsde);


def registro_docente(request):
    html_responsde = "<h1>Registro de docente</h1>"
    html_responsde = html_base + html_responsde
    return HttpResponse(html_responsde);


def modificaciona(request):
    html_responsde = "<h1>Registro de docente</h1>"
    html_responsde = html_base + html_responsde
    return HttpResponse(html_responsde);


def reporte(request):
    html_responsde = "<h1>REPORTE</h1>"
    html_responsde = html_base + html_responsde
    return HttpResponse(html_responsde);


def vacaciones(request):
    html_responsde = "<h1>VACACIONES</h1>"
    html_responsde = html_base + html_responsde
    return HttpResponse(html_responsde);


def home(request, plantilla="home.html"):
    return render(request, plantilla);


def empleados(request, plantilla="empleados.html"):
    return render(request, plantilla);


def horario(request, plantilla="horario.html"):
    return render(request, plantilla);


def modificacion(request, plantilla="modificacion.html"):
    return render(request, plantilla);


def asistencia(request, plantilla="asistencia.html"):
    return render(request, plantilla);


def registro_docente(request, plantilla="registro_docente.html"):
    return render(request, plantilla);


def modificaciona(request, plantilla="registro_docente.html"):
    return render(request, plantilla);


def reporte(request, plantilla="reporte.html"):
    return render(request, plantilla);


def vacaciones(request, plantilla="vacaciones.html"):
    return render(request, plantilla);
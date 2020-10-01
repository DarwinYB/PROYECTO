from django.db import models


# Create your models here.

# Create your models here.

class Asistencia(models.Model):
    nombre = models.CharField(max_length=200)
    apellido = models.CharField(max_length=200)
    jornada = models.CharField(max_length=200)
    estado = models.IntegerField(default=1)  # 1 es activo -------y 2 eliminado
    user = models.CharField(max_length=20)
    user_mod = models.CharField(max_length=20)
    entrada = models.DateTimeField(auto_now_add=True)
    created = models.DateTimeField(auto_now_add=True)
    salida = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'Asistencia'
        verbose_name = "asistencia"
        verbose_name_plural = "asistencias"

    def __str__(self):
        return "{} {} {} {} {}".format(self.nombre, self.apellido, self.jornada, self.entrada, self.salida)


class Semana(models.Model):
    dias = models.CharField(max_length=30)
    user = models.CharField(max_length=15)
    user_mod = models.CharField(max_length=15)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = "Dias"
        verbose_name = "Dia"
        verbose_name_plural = "Dias"

    def __str__(self):
        return self.dias


class Horario(models.Model):
    dias = models.ForeignKey(Semana, null=True, blank=True, on_delete=models.CASCADE)
    Hora_entrada = models.TimeField()
    Hora_Salida = models.TimeField()
    user = models.CharField(max_length=15)
    user_mod = models.CharField(max_length=15)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = "Horarios"
        verbose_name = 'Horario'
        verbose_name_plural = 'Horarios'

    def __str__(self):
        return "{} {} {} ".format(self.dias, self.Hora_entrada, self.Hora_Salida)


class Vacaciones(models.Model):
    Nombre = models.CharField(max_length=200)
    Apellido = models.CharField(max_length=200)
    email = models.EmailField(default="@est.itsgg.edu.ec")
    Fecha_Inicio = models.DateField()
    Fecha_Culminacion = models.DateField()
    user = models.CharField(max_length=15)
    user_mod = models.CharField(max_length=15)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = "Vacaciones"

    def __str__(self):
        return "{} {} {} {}".format(self.Nombre, self.Apellido, self.Fecha_Inicio, self.Fecha_Culminacion)
# Create your models here.


class Reportes(models.Model):
    Fecha_Reporte = models.DateTimeField(auto_now_add=False)
    Ced_Empleado = models.CharField(max_length=10)
    Nombre = models.CharField(max_length=200)
    Apellido = models.CharField(max_length=200)
    Area = models.CharField(max_length=100)

    class Meta:
        db_table = "Reportes"

    def __str__(self):
        return "{} {} {} {} {}".format(self.Fecha_Reporte, self.Ced_Empleado, self.Nombre, self.Apellido, self.Area)



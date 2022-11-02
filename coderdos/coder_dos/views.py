
from django.http import HttpResponse

from datetime import datetime

from django.template import Template, Context

def vista_plantilla(request):
    # Abrimos el archivo
    archivo = open(r"C:/Users/JuanCarlos/Desktop/Python/Clase2_Django/coderdos/coder_dos/Templates/planilla.html")

    # Creamos el objeto "plantilla"
    plantilla = Template(archivo.read())

    # Cerramos el archivo para liberar recursos
    archivo.close()

    # Diccionario con datos para la plantilla
    datos = {"nombre": "Leonel", "fecha": datetime.now(), "apellido": "Gareis"}

    # Creamos el contexto
    contexto = Context(datos)

    # Renderizamos la plantilla para crear la respuesta
    documento = plantilla.render(contexto)

    # Retornamos la respuesta
    return HttpResponse(documento)

def vista_listado_alumnos(request):

    # Abrimos el archivo
    archivo = open("C:/Users/JuanCarlos/Desktop/Python/Clase2_Django/coderdos/coder_dos/Templates/planilla.html")

    # Creamos el template
    plantilla = Template(archivo.read())

    # Cerramos el archivo para liberar recursos
    archivo.close()

    # Creamos el diccionario de datos
    listado_alumnos = ["Leonel Gareis", "Agustin Russo", "Cristian Garcia", "Angelo Pettinari", "Diego Ibarra", "Santiago Ortiz", "Barbara Vivante",  "Barbara Pino"]


    datos = {"tecnologia": "React", "listado_alumnos": listado_alumnos}

    # Creamos el contexto
    contexto = Context(datos)

    documento = plantilla.render(contexto)

    return HttpResponse(documento)


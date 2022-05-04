from django.http import HttpResponse
import datetime
from django.template import Template, Context

class Persona(object):

  def __init__(self, nombre, apellido):

    self.nombre=nombre

    self.apellido=apellido

def saludo(request): #Primera vista

  return HttpResponse("<html><body><h1>Hola mundo uso Django</h1></body></html")
  #Probar la pagina(iniciar el server):vamos al cmd, cd *Ruta del proyecto*,python manage.py runserver
  #Entrar a la pagina: localhost:8000/saludo/
def despedida(request): #segunda vista
  p1 = Persona("Victor", "Hernández")

  #nombre="Joshua" 
  #apellido="Hernández"

  tiempofecha=datetime.datetime.now()

  doc_externo=open("C:/Users/Joshua/Desktop/Django/Proyecto1/Proyecto1/Plantillas/miplantilla.html")
#doc_externo:la variable    cargando un documento externo con su ruta de forma manual
  plt=Template(doc_externo.read())
#plt variable    objeto de tipo template que leé el documento que esta en doc_externo
  doc_externo.close()
#Se cierra la comunicación luego de ya haberlo cargado para ahorrar recursos 
  ctx=Context({"nombre_persona":p1.nombre,"apellido_persona":p1.apellido,"tiempo_actual":tiempofecha, "temas":["Plantillas","Modelos","Formularios","Vistas","Despliegue"]})
#ctx varable con la que se crea el contexto
  documento=plt.render(ctx)
  #documento variable con la que se renderiza el contexto , se almacena el renderizado utilizando plt
  #  donde esta el documento almacenado y luego se llama al render y se le pasa el context
  return HttpResponse(documento)

def new_func():
    p1=Persona("Victor", "Ramón")
    return p1

def damefecha(request):
  fecha_actual=datetime.datetime.now()
  documento="""<html>
  <body>
  <h1>
  Fecha y hora actuales %s
  </h1>
  </body>
  </html""" %fecha_actual
  
  return HttpResponse(documento)

def calculaEdad(request, edad, agno):
  #edadActual=18
  periodo=agno-2022
  edadFutura=edad+periodo
  documento="<html><body><h2>En el año %s tendras %s años" %(agno, edadFutura)
  return HttpResponse(documento)
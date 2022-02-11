from contextvars import Context
from django.http import HttpResponse
from django.template import Template, Context
from django.template import loader
from datetime import datetime
def saludo(request):
    return HttpResponse("<h1>Hola Mundo!</h1>")

def chau(request):
    return HttpResponse('<h2>Nos vemos!</h1>')

def hoy(request):
    _hoy = datetime.now()
    return HttpResponse(f'Hoy es {_hoy}')

def saludar_a(request, nombre):
    return HttpResponse(f'Hola  {nombre}')

def ejemplo_template(request):
    diccionario = {'nombre': 'Martin',
    'apellido': 'Gotelli',
    'hoy': datetime.now(),
    'notas': [2, 4, 4, 8, 2, 3],
    }
    # template_html = open('Proyecto1/templates/ejemplo.html')
    # template = Template(template_html.read())
    # template_html.close()
    # contexto = Context(diccionario)
    template = loader.get_template('ejemplo.html')
    documento = template.render(diccionario)
    return HttpResponse(documento)

def cuando_naci(request, edad):
    nacimiento = (datetime.now().year - int(edad))  
    return HttpResponse(f'<h1>Hola, naciste en el año {nacimiento} </h1>')
    


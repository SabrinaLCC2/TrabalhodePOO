from django.shortcuts import render
from user_agents import parse 
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from app.models import Paciente, Medico, Atendente, Consultas
from django.contrib.auth.backends import BaseBackend


def index(request,identificador):
    REMOTE_ADDR = request.META.get('REMOTE_ADDR')
    HTTP_HOST = request.META.get('HTTP_HOST')
    HTTP_ACCEPT_LANGUAGE = request.META.get('HTTP_ACCEPT_LANGUAGE')
    linguagem_preferida = HTTP_ACCEPT_LANGUAGE.split(",")
    HTTP_USER_AGENT_string = request.META.get('HTTP_USER_AGENT')
    navegador = parse(HTTP_USER_AGENT_string)

    dados = {'nome':'Fabricio', 'sobrenome':'Leite','id':identificador,'ip':REMOTE_ADDR,'host':HTTP_HOST,'linguagem':HTTP_ACCEPT_LANGUAGE,'linguagem_preferida': linguagem_preferida[0],'navegador':navegador.browser.family,'so':navegador.os.family+navegador.os.version_string}
    
    return render(request,'index.html',dados)


def pagina_estatica(request):
    return render(request,'pagina_estatica.html')

def home(request):
    nome = "Cleisson"  # Certifique-se de que `nome_completo` existe no modelo Atendente
    dados = {'nome_completo': nome, 'pagina': 'home'}
    return render(request, 'home.html', dados)

def paciente(request):
    lista_pacientes = Paciente.objects.all()
    lista_paginada = Paginator(lista_pacientes,7)
    numero_pagina = request.GET.get('p')
    try:
        pagina = lista_paginada.page(numero_pagina)
    except PageNotAnInteger:
        pagina = lista_paginada.page(1)
    except EmptyPage:
        pagina = lista_paginada.page(1)
    
    dados = {'pagina': 'paciente', 'lista_pacientes': pagina}
    return render(request, 'paciente.html', dados)

def detalhamento_paciente(request,id):
    dados = {'paciente':Paciente.objects.get(id=id),'pagina':'paciente','consultas':Consultas.objects.filter(paciente_id=id)}
    return render(request,'detalhamento_paciente.html',dados)

def medico(request):
    lista_medicos = Medico.objects.all()
    lista_paginada = Paginator(lista_medicos,7)
    numero_pagina = request.GET.get('p')
    try:
        pagina = lista_paginada.page(numero_pagina)
    except PageNotAnInteger:
        pagina = lista_paginada.page(1)
    except EmptyPage:
        pagina = lista_paginada.page(1)
    
    dados = {'pagina': 'medico', 'lista_medicos': pagina}
    return render(request, 'medico.html', dados)

def detalhamento_medico(request,id):
    dados = {'pagina':'medico','medico':Medico.objects.get(id=id),'consultas': Consultas.objects.filter(medico_id=id)}
    
    return render(request,'detalhamento_medico.html',dados)

def atendente(request):
    lista_atendentes = Atendente.objects.all()
    lista_paginada = Paginator(lista_atendentes,7)
    numero_pagina = request.GET.get('p')
    try:
        pagina = lista_paginada.page(numero_pagina)
    except PageNotAnInteger:
        pagina = lista_paginada.page(1)
    except EmptyPage:
        pagina = lista_paginada.page(1)
    
    dados = {'pagina': 'atendente', 'lista_atendentes': pagina}
    return render(request, 'atendente.html', dados)


def consulta(request):
    lista_consultas = Consultas.objects.all()
    lista_paginada = Paginator(lista_consultas,7)
    numero_pagina = request.GET.get('p')
    try:
        pagina = lista_paginada.page(numero_pagina)
    except PageNotAnInteger:
        pagina = lista_paginada.page(1)
    except EmptyPage:
        pagina = lista_paginada.page(1)
    
    dados = {'pagina': 'consulta', 'lista_consultas': pagina}
    return render(request, 'consulta.html', dados)

def detalhamento_consulta(request,id):
    dados = {'pagina':'consulta','consulta':Consultas.objects.get(id=id)}
    return render(request,'detalhamento_consulta.html',dados)
    

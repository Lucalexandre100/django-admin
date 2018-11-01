from django.http import HttpResponse
from django.shortcuts import render

def home(request):
    sexo = 'm'
    nome = 'Alfredo'

    lista = [
        {'nome': 'Lucas', 'sexo': 'm'},
        {'nome': 'Suelen', 'sexo': 'f'},
        {'nome': 'Joaquina', 'sexo': 'f'},
        {'nome': 'Joao', 'sexo': 'm'},
    ]


    dados = {'lista': lista, 'sexo': sexo, 'nome': nome}

    return render(request, 'index.html', dados)


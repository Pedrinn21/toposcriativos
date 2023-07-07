from django.shortcuts import render
from django.http import HttpResponse
from .models import *

def list(request):
    data = {}
    data['db'] = TipoPapel.objects.all()
    return render(request, 'tipopapel_list.html', data)

def insert(request):
    if request.method == "POST":
        descricao = request.POST.get('descricao')
        
        tipopapel = TipoPapel(descricao=descricao)

        tipopapel.save()

        return list(request)
    
    elif request.method == "GET":
        return render(request, 'tipopapel_insert.html')

def save(request):
    return HttpResponse('Tipo papel Salvo')

def update(request):
    return HttpResponse('Aqui vai ser a update do tipopapel')

def delete(request):
    return HttpResponse('Aqui vai ser a delete do tipopapel')
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

def update(request, id):
    if request.method == "POST":

        descricao = request.POST.get('descricao')
        print("Descricao:" + descricao)

        tipopapel = TipoPapel(id=id, descricao=descricao)

        tipopapel.save()

        return list(request)

    elif request.method == "GET":

        print (id)
        data = {}
        data['tipopapel'] = TipoPapel.objects.get(id=id)
        
        print(data)

        return render(request, 'tipopapel_update.html', data)

def delete(request, id):

    tipopapel = TipoPapel.objects.get(id=id)
    tipopapel.delete()

    return list(request)
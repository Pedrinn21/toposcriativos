from django.shortcuts import render
from tipopapel import models
from .models import *

def list(request):
    data = {}
    data['materiaprima'] = MateriaPrima.objects.all()
    return render(request, 'materiaprima_list.html', data)

def insert(request):
    if request.method == "POST":

        gramatura = request.POST.get('gramatura')
        #print("gramatura:" + gramatura)

        quantidade = request.POST.get('quantidade')
        #print("quantidade:" + quantidade)

        idtipopapel = request.POST.get('tipopapel')
        print("ID Tipo papel:" + idtipopapel)

        materiaprima = MateriaPrima(fktipopapel_id=idtipopapel, gramatura=gramatura, quantidade=quantidade)

        materiaprima.save()

        return list(request)


    elif request.method == "GET":
        data = {}
        data['tipopapel'] = TipoPapel.objects.all()
        return render(request, 'materiaprima_insert.html', data)

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

    materiaprima = MateriaPrima.objects.get(id=id)
    materiaprima.delete()

    return list(request)
from django.shortcuts import render
from tipopapel import models
from .models import *
from django.http import HttpResponse

def list(request):
    data = {}
    data['materiaprima'] = MateriaPrima.objects.all()
    print(data)
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
        #Pega o tipo de papel enviado pela requisição
        tipopapel = request.POST.get('tipopapel')
        print(tipopapel)

        #Pega a gramatura enviado pela requisição
        gramatura = request.POST.get('gramatura')
        print(gramatura)

        #Pega a quantidade enviado pela requisição
        quantidade = request.POST.get('quantidade')
        print(quantidade)

        materiaprima = MateriaPrima(id=id, fktipopapel_id=tipopapel, gramatura=gramatura, quantidade=quantidade)

        materiaprima.save()

        return list(request)

    elif request.method == "GET":
        print (id)
        data = {}
        data['materiaprima'] = MateriaPrima.objects.get(id=id)
        data['tipopapel'] = TipoPapel.objects.all()
        
        print(data)

        return render(request, 'materiaprima_update.html', data)


def delete(request, id):

    materiaprima = MateriaPrima.objects.get(id=id)
    materiaprima.delete()

    return list(request)
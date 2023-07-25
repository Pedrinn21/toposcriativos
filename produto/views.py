from django.http import HttpResponseRedirect
from django.urls import reverse
from django.shortcuts import render
from .models import *


def list(request):
    data = {}
    data['produto'] = Produto.objects.all()
    print(data)
    return render(request, 'produto_list.html', data)

def insert(request):
    if request.method == "POST":

        gasto = request.POST.get('gasto')
        print("gasto:" + gasto)

        valor = request.POST.get('valor')
        print("valor:" + valor)

        idtipoproduto = request.POST.get('tipoproduto')
        print("ID Tipo produto:" + idtipoproduto)

        idmateriaprima = request.POST.get('materiaprima')
        print("ID materia prima:" + idmateriaprima)

        #materiaprima = MateriaPrima(fktipopapel_id=idtipopapel, gramatura=gramatura, quantidade=quantidade)

        #materiaprima.save()

        return redirect()


    elif request.method == "GET":
        data = {}
        data['tipoproduto'] = TipoProduto.objects.all()
        data['materiaprima'] = MateriaPrima.objects.all()
        print(data)
        return render(request, 'produto_insert.html', data)

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

        return redirect()

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

    return redirect()

def redirect():
    return HttpResponseRedirect(reverse('produto.list'))
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.shortcuts import render
from .models import *

def list(request):
    data = {}
    data['tipoproduto'] = TipoProduto.objects.all()
    return render(request, 'tipoproduto_list.html', data)

    
def redirect():
    return HttpResponseRedirect(reverse('tipoproduto.list'))

def insert(request):
    if request.method == "POST":
        descricao = request.POST.get('descricao')
        
        tipoproduto = TipoProduto(descricao=descricao)

        tipoproduto.save()

        return redirect()
    
    elif request.method == "GET":
        return render(request, 'tipoproduto_insert.html')

def update(request, id):
    if request.method == "POST":

        descricao = request.POST.get('descricao')
        print("Descricao:" + descricao)

        tipoproduto = TipoProduto(id=id, descricao=descricao)

        tipoproduto.save()

        return redirect()

    elif request.method == "GET":

        print (id)
        data = {}
        data['tipoproduto'] = TipoProduto.objects.get(id=id)
        
        print(data)

        return render(request, 'tipoproduto_update.html', data)

def delete(request, id):

    tipoproduto = TipoProduto.objects.get(id=id)
    tipoproduto.delete()

    return redirect()
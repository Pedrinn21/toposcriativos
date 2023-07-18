from django.http import HttpResponseRedirect
from django.urls import reverse
from django.shortcuts import render
from .models import *

def list(request):
    data = {}
    data['tipopapel'] = TipoPapel.objects.all()
    return render(request, 'tipopapel_list.html', data)

    
def redirect():
    return HttpResponseRedirect(reverse('tipopapel.list'))

def insert(request):
    if request.method == "POST":
        descricao = request.POST.get('descricao')
        
        tipopapel = TipoPapel(descricao=descricao)

        tipopapel.save()

        return redirect()
    
    elif request.method == "GET":
        return render(request, 'tipopapel_insert.html')

def update(request, id):
    if request.method == "POST":

        descricao = request.POST.get('descricao')
        print("Descricao:" + descricao)

        tipopapel = TipoPapel(id=id, descricao=descricao)

        tipopapel.save()

        return redirect()

    elif request.method == "GET":

        print (id)
        data = {}
        data['tipopapel'] = TipoPapel.objects.get(id=id)
        
        print(data)

        return render(request, 'tipopapel_update.html', data)

def delete(request, id):

    tipopapel = TipoPapel.objects.get(id=id)
    tipopapel.delete()

    return redirect()
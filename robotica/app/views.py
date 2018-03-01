from .models import Punti, Mappa, Grafico, Nome
from django.shortcuts import render
from django.shortcuts import render
from django.utils import timezone
from django.shortcuts import get_object_or_404, render
from .forms import MappaForm, AmpiezzaForm, NomeForm
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.http import JsonResponse
from django.contrib.auth import authenticate, login
from django.contrib.auth import logout
from django.views.decorators.csrf import csrf_protect
import datetime
from django.db.models import Q
from django.forms import formset_factory
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.http import HttpResponse
from django.template import Context
from django.template.loader import render_to_string, get_template
from django.core.mail import EmailMessage
from django.core.mail import send_mail
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from django.db.models import Count
from django.contrib.postgres.search import SearchVector
from django.db.models import Q
from django.contrib.auth.models import User
from django.contrib.auth.validators import ASCIIUsernameValidator
from django.template.loader import render_to_string
from django.http import Http404
from django.contrib import messages
import os
import sys

def grafici (request):
    ampiezza= AmpiezzaForm(request.POST)#lettura html dell'ampiezza
    nome= NomeForm(request.POST)#lettura html del nome mappa



    if request.method == "POST":
        messages.success(request, 'Griglia Creata Con Successo.')  #messaggio di successo
        ampiezzaInt=int(request.POST.get("ampiezza"))  #richiesta del numero intero inserito prima all'interno dell'html
        nome.nome_mappa=nome   #selezione e salvataggio nella tabella Nome del capom nome
        nome.save()
        nome=(request.POST.get("nome_mappa")) #estrapolazione del nome dall'html
        nome= Nome.objects.get(nome_mappa=nome)#estrapolazione dell'id dal nome... Attenzione: se ci sono 2 o piu nomi uguali bugga tutto


#creazione di una griglia che si espande nelle 4 direzioni di un piano cartesiano con ampiezza ripetuta per ogni quadrante 
        for y in range(ampiezzaInt):
            for x in range(ampiezzaInt):
                form = MappaForm(request.POST)
                if form.is_valid():
                    mappa = form.save(commit=False)
                    mappa.x= x
                    mappa.y= y
                    mappa.nome_mappa=nome
                    mappa.save()
        for y in range(ampiezzaInt):
            for x in range(ampiezzaInt):
                form = MappaForm(request.POST)
                if form.is_valid():
                    mappa = form.save(commit=False)
                    mappa.x= -x
                    mappa.y= -y
                    mappa.nome_mappa=nome
                    mappa.save()
        for y in range(ampiezzaInt):
            for x in range(ampiezzaInt):
                form = MappaForm(request.POST)
                if form.is_valid():
                    mappa = form.save(commit=False)
                    mappa.x= x
                    mappa.y= -y
                    mappa.nome_mappa=nome
                    mappa.save()
        for y in range(ampiezzaInt):
            for x in range(ampiezzaInt):
                form = MappaForm(request.POST)
                if form.is_valid():
                    mappa = form.save(commit=False)
                    mappa.x= -x
                    mappa.y= y
                    mappa.nome_mappa=nome
                    mappa.save()


    else:
        form = MappaForm()
        ampiezza= AmpiezzaForm()
        nome= NomeForm()

    listaMappe= Nome.objects.all()





    return render(request, 'grafici.html', {'form':form, 'ampiezza':ampiezza, 'listaMappe': listaMappe, 'nome': nome })

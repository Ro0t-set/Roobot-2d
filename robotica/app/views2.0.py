from .models import Punti, Mappa, Grafico, Nome
from django.shortcuts import render
from django.shortcuts import render
from django.utils import timezone
from django.shortcuts import get_object_or_404, render
from .forms import MappaForm, AmpiezzaForm, NomeForm, DensitàForm
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.http import JsonResponse
from django.contrib.auth import authenticate, login
from django.contrib.auth import logout
from django.views.decorators.csrf import csrf_protect
import datetime
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.db.models import Q
from django.forms import formset_factory
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.http import HttpResponse
from django.template import Context
from django.template.loader import render_to_string, get_template
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
import math
import importlib
import threading
from queue import Queue
import time
import serial



def grafici (request):
    listaMappe= Nome.objects.all()
    mappa=  Mappa.objects.all()

    page = request.GET.get('page')

    paginator = Paginator(listaMappe, 1) # Show 1 contacts per page
    try:
        listaMappe = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        listaMappe = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        listaMappe = paginator.page(paginator.num_pages)


    idMappa=listaMappe.object_list.values_list('id', flat=True)
    mappaSingola = Mappa.objects.filter(nome_mappa=idMappa)


    ampiezza= AmpiezzaForm(request.POST)#lettura html dell'ampiezza
    nome= NomeForm(request.POST)#lettura html del nome mappa
    #idMappa= request.POST['mappaId']
    # print(idMappa)
    if 'resetta_mappatura' in request.POST :
        postamentoX=0
        spostamentoY=0
        for mappaSingola in mappaSingola:
            if mappaSingola.aggettivo != 1:
               mappaSingola.delete()


    if 'inizza_mappatura' in request.POST :
        densità = DensitàForm(request.POST)


        if densità.is_valid():
            denditàInt=int(request.POST.get("densità"))
            print("denzità:",denditàInt)
            rivelazioni=360/denditàInt
        else:
            densità=DensitàForm()
        nome= Nome.objects.get(id=idMappa)#estrapolazione dell'id dal nome... Attenzione: se ci sono 2 o piu nomi uguali bugga tutto
        spostamentoX=0
        spostamentoY=0
        r=0
        while r<2:
            r=r+1
            Rad180=math.pi
            a=0
            angle = 0
            nome= Nome.objects.get(id=idMappa)#estrapolazione dell'id dal nome... Attenzione: se ci sono 2 o piu nomi uguali bugga tutto

            ser = serial.Serial ('/dev/ttyACM0',)
            ser.baudrate = 115200
            print ('Using SerialPort:')
            print (ser.name)
            print(ser.readline())
            ser.write(str(denditàInt).encode())
            ser.write(str('\n').encode())
            print(ser.readline())

            while ser.readline().strip()!=str('end').encode():
                distance=float(ser.readline().strip())


                angleRad= angle*(math.pi)/180#calcolo angoli motore in radianti
                if a%2 == 0:
                    x = int((math.cos(angleRad)*distance)+spostamentoX)#creazione x e y per mezzo di seno e coseno, da lettura a cerchio a piano cartesiano
                    y = int((math.sin(angleRad)*distance)+spostamentoY)
                else:
                    x = int((math.cos(angleRad+Rad180)*distance)+spostamentoX)#creazione x e y per mezzo di seno e coseno, da lettura a cerchio a piano cartesiano
                    y = int((math.sin(angleRad+Rad180)*distance)+spostamentoY)
                    angle=angle+denditàInt
                if distance<100:
                    Mappa.objects.create(x=x, y=y, nome_mappa=nome, aggettivo=3)#salvataggio dati

                if name == 'main':
                    sys.exit(main())
                a=a+1

            distanzaMaxList=[Serial.read0,Serial.read1,Serial.read30,Serial.read3]
            Mappa.objects.create(x=spostamentoX, y=spostamentoY, nome_mappa=nome, aggettivo=10)
            distanceMax=max(distanzaMaxList)
            print("distanza massima:",distanceMax)
            if distanceMax==Serial.read0:
                spostamentoX=spostamentoX+(int(distanceMax/2))
                print("avanti")
            elif distanceMax==Serial.read1:
                spostamentoX=spostamentoX-(int(distanceMax/2))
                print("indietro")
            elif distanceMax==Serial.read32:
                spostamentoY=spostamentoY+(int(distanceMax/2))
                print("destra")
            elif distanceMax==Serial.read30:
                spostamentoY=spostamentoY-(int(distanceMax/2))
                print("sinistra")
            print("spostamento x:",spostamentoX)
            print("spostamento y:",spostamentoY)






    if 'creazione_mappa' in request.POST :
        messages.success(request, 'Griglia Creata Con Successo.')  #messaggio di successo
        # ampiezzaInt=int(request.POST.get("ampiezza"))  #richiesta del numero intero inserito prima all'interno dell'html
        nome.nome_mappa=nome   #selezione e salvataggio nella tabella Nome del capom nome
        nome.save()
        nome=(request.POST.get("nome_mappa")) #estrapolazione del nome dall'html
        nome= Nome.objects.get(nome_mappa=nome)#estrapolazione dell'id dal nome... Attenzione: se ci sono 2 o piu nomi uguali bugga tutto


#creazione di una griglia che si espande nelle 4 direzioni di un piano cartesiano con ampiezza ripetuta per ogni quadrante
        # for y in range(0, ampiezzaInt):
        #     for x in range(0, ampiezzaInt):
        #         form = MappaForm(request.POST)
        #         if form.is_valid():
        #             mappa = form.save(commit=False)
        #             mappa.x= x
        #             mappa.y= y
        #             mappa.nome_mappa=nome
        #             mappa.save()
        # for y in range(0, ampiezzaInt):
        #     for x in range(0, ampiezzaInt):
        #         form = MappaForm(request.POST)
        #         if form.is_valid():
        #             mappa = form.save(commit=False)
        #             mappa.x= -x
        #             mappa.y= -y
        #             mappa.nome_mappa=nome
        #             mappa.save()
        # for y in range(0, ampiezzaInt):
        #     for x in range(0, ampiezzaInt):
        #         form = MappaForm(request.POST)
        #         if form.is_valid():
        #             mappa = form.save(commit=False)
        #             mappa.x= x
        #             mappa.y= -y
        #             mappa.nome_mappa=nome
        #             mappa.save()
        # for y in range(0, ampiezzaInt):
        #     for x in range(0, ampiezzaInt):
        #         form = MappaForm(request.POST)
        #         if form.is_valid():
        #             mappa = form.save(commit=False)
        #             mappa.x= -x
        #             mappa.y= y
        #             mappa.nome_mappa=nome
        #             mappa.save()

    else:
        form = MappaForm()
        ampiezza= AmpiezzaForm()
        nome= NomeForm()
        densità=DensitàForm()

    scalo=1

    x= (list(Mappa.objects.filter(nome_mappa=idMappa, aggettivo=3 ).values_list('x', flat=True)))
    y= (list(Mappa.objects.filter(nome_mappa=idMappa, aggettivo=3).values_list('y', flat=True)))
    posizioneX=(list(Mappa.objects.filter(nome_mappa=idMappa, aggettivo=10).values_list('x', flat=True)))
    posizioneY= (list(Mappa.objects.filter(nome_mappa=idMappa, aggettivo=10).values_list('y', flat=True)))

    if x != []:
        maxYX=[(max(x)),(max(y)),-(min(x)),-(min(y))]
        maxYX=(max(maxYX))
    else:
        maxYX=100

    a=0
    xyhtml=""
    for x in x:
        xy=int(x/scalo)
        xy=str(xy)
        yx=int(y[a])
        yx=yx/scalo
        yx=str(y[a])
        xyhtml=str(xyhtml)+str("{x:"+(xy)+",y:"+ (yx)+", r: 4},")
        a=a+1

    a=0
    posizionehtml=""
    print(posizioneY)
    for posizioneX in posizioneX:
        posixioneXY=int(posizioneX/scalo)
        posixioneXY=str(posixioneXY)
        posizioneYX=int(posizioneY[a])
        posizioneYX=str(posizioneY[a])
        posizionehtml=str(posizionehtml)+str("{x:"+(posixioneXY)+",y:"+ (posizioneYX)+", r: 7},")
        a=a+1



    return render(request, 'grafici.html', {'maxYX':maxYX, 'densità':densità, 'ampiezza':ampiezza, 'listaMappe': listaMappe, 'nome': nome, 'xyhtml':xyhtml, 'posizionehtml':posizionehtml})

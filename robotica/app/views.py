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
from django.views.decorators.csrf import csrf_protect
import datetime
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
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
from django.contrib import messages
from django.db.models import Count
import os
import sys
import math
import importlib
import threading
from queue import Queue
import time
#import movimento
from movimento import avanti, indietro, destra, sinistra


def grafici (request):
    listaMappe= Nome.objects.all()
    mappa=  Mappa.objects.all()
    direzione= ""
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

            denditàInt=int(15)
            print("denzità:",denditàInt)
            rivelazioni=360/denditàInt

            nome= Nome.objects.get(id=idMappa)#estrapolazione dell'id dal nome... Attenzione: se ci sono 2 o piu nomi uguali bugga tutto
            spostamentoX=0
            spostamentoY=0
            r=0
            while r<5:
                r=r+1



                try:
                    Reload = importlib.reload(Serial)
                except:
                    import Serial

                Rad180=math.pi
                a=0
                angle = 0
                nome= Nome.objects.get(id=idMappa)#estrapolazione dell'id dal nome... Attenzione: se ci sono 2 o piu nomi uguali bugga tutto


                while a<rivelazioni:
                    a=str(a)
                    distance="read"+a
                    distance="Serial."+distance
                    distance=eval(distance)#lettura distanza
                    distance=int(distance)
                    a=int(a)
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
                    a= a+1

                Grad90 =int(360/denditàInt/2)
                Grad90= str(Grad90)

                novanta="Serial.read"+Grad90
                novanta=eval(novanta)
                Grad90piuuno=str(int(Grad90)+1)
                centoottanta="Serial.read"+Grad90piuuno
                centoottanta=eval(centoottanta)

                distanzaMaxList=[Serial.read0,Serial.read1, novanta, centoottanta]
                Mappa.objects.create(x=spostamentoX, y=spostamentoY, nome_mappa=nome, aggettivo=10)
                distanceMax=max(distanzaMaxList)
                print("distanza massima:",distanceMax)



                if distanceMax==Serial.read0 and direzione != "indietro":
                    spostamentoX=spostamentoX+(int(distanceMax/2))
                    direzione="avanti"
                    print("avanti")
                    avanti(5)

                elif distanceMax==Serial.read1 and direzione != "avanti":
                    direzione="indietro"
                    spostamentoX=spostamentoX-(int(distanceMax/2))
                    print("indietro")
                    indietro(5)

                elif distanceMax==novanta:
                    direzione="avanti"
                    spostamentoY=spostamentoY+(int(distanceMax/2))
                    print("destra")
                    destra(5)

                elif distanceMax==centoottanta:
                    direzione="avanti"
                    spostamentoY=spostamentoY-(int(distanceMax/2))
                    print("sinistra")
                    sinistra(5)



                print("spostamento x:",spostamentoX)
                print("spostamento y:",spostamentoY)





    if 'creazione_mappa' in request.POST :
        nome= NomeForm(request.POST)
        if nome.is_valid():
            messages.success(request, 'Griglia Creata Con Successo.')  #messaggio di successo
            # ampiezzaInt=int(request.POST.get("ampiezza"))  #richiesta del numero intero inserito prima all'interno dell'html
            nome.nome_mappa=nome   #selezione e salvataggio nella tabella Nome del capom nome
            nome.save()

        else:
            nome= NomeForm()




    x= (list(Mappa.objects.filter(nome_mappa=idMappa, aggettivo=3 ).values_list('x', flat=True)))
    y= (list(Mappa.objects.filter(nome_mappa=idMappa, aggettivo=3).values_list('y', flat=True)))
    posizioneX=(list(Mappa.objects.filter(nome_mappa=idMappa, aggettivo=10).values_list('x', flat=True)))
    posizioneY= (list(Mappa.objects.filter(nome_mappa=idMappa, aggettivo=10).values_list('y', flat=True)))

    nRilevazioni=(Mappa.objects.filter(nome_mappa=idMappa, aggettivo=3))


    if x != []:
        maxYX=[(max(x)),(max(y)),-(min(x)),-(min(y))]
        maxYX=(max(maxYX))
    else:
        maxYX=100

    a=0
    xyhtml=""
    for x in x:
        xy=int(x)
        xy=str(xy)
        yx=int(y[a])
        yx=yx
        yx=str(y[a])
        xyhtml=str(xyhtml)+str("{x:"+(xy)+",y:"+ (yx)+", r: 4},")
        a=a+1

    a=0
    posizionehtml=""
    print(posizioneY)
    for posizioneX in posizioneX:
        posixioneXY=int(posizioneX)
        posixioneXY=str(posixioneXY)
        posizioneYX=int(posizioneY[a])
        posizioneYX=str(posizioneY[a])
        posizionehtml=str(posizionehtml)+str("{x:"+(posixioneXY)+",y:"+ (posizioneYX)+", r: 7},")
        a=a+1



    return render(request, 'grafici.html', {'maxYX':maxYX, 'nRilevazioni':nRilevazioni, 'ampiezza':ampiezza, 'listaMappe': listaMappe, 'nome': nome, 'xyhtml':xyhtml, 'posizionehtml':posizionehtml})

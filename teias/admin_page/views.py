from django.shortcuts import render,HttpResponse
import pandas as pd
from .models import *
from .models import personel
from django.core.mail import send_mail
from django.http import JsonResponse
from django.db.models import Count
import sqlite3
import pandas as pd


def index(request):                       #initial page for my project
    return render(request,"index.html")


def login(request):                       #loading to login page
    return render(request, "login.html")


def main(request):                        #checking correct user
    liste = sifre.objects.all()
    val1=request.GET["username"]
    val2=request.GET["password"]
    a=0
    for i in liste:
        if (i.KULLANICI== val1 and i.SİFRE == val2):
            a=1
            return render(request, "main.html")
    if a==0:
        return render(request, "login.html")




def personel(request):                           #loading personel page
    return render(request, "personel.html")



def show(request):                              #showing data from database like table
     liste = donanım_dbs.objects.order_by("id")
     context = {"liste": liste}
     return render(request, "show.html", context)



def show_2(request):                         #reading data and updating data
    conn = sqlite3.connect('db.sqlite3')
    c = conn.cursor()

    liste = donanım_dbs.objects.order_by("id")
    context = {"liste": liste}
    if request.GET["ek"]:

        liste = donanım_dbs.objects.order_by("id")
        val1 = request.GET["ek"]
        val1=val1.split("/")



        c.execute("UPDATE admin_page_personel  SET AD_SOYAD=?,DEPARTMAN=? WHERE id=? ",(val1[1],val1[2],val1[0]))
        c.execute("UPDATE admin_page_donanım_dbs  SET DURUM=? WHERE EVENT_id=? ", (val1[3], val1[0]))

        conn.commit()

        c.close()

        context = {"liste": liste, "a": val1[1]}
        return render(request, "show.html", context)
    else:
        return render(request, "show.html", context)


def show_3(request):
     conn = sqlite3.connect('db.sqlite3')
     c = conn.cursor()


     liste = donanım_dbs.objects.all()


     ad = request.GET["ad"]
     departman = request.GET["departman"]
     tür = request.GET["tür"]
     marka = request.GET["marka"]
     model = request.GET["model"]
     seri_no = request.GET["seri_no"]
     lokasyon = request.GET["lokasyon"]
     durum = request.GET["durum"]
     context = {"liste": liste}
     look=0
     a=c.execute("SELECT * FROM admin_page_personel  ")
     a = a.fetchall()
     for i in a:

         if (i[1] == ad):
                  context = {"liste": liste, "x": i[1]}
                  look=1
                  c.execute(
             "INSERT INTO admin_page_donanım_dbs (TUR,MARKA,MODEL,SERI_NO,DURUM,LOKASYON,EVENT_id) VALUES (?,?,?,?,?,?,?) ",
             (tür, marka, model, seri_no , lokasyon, durum, i[0]))
                  break
     if look==0:
         c.execute("INSERT INTO admin_page_personel ( AD_SOYAD,DEPARTMAN) VALUES (?,?) ",
                   (ad, departman))

     if look==0:


         #a=c.execute("SELECT id from  admin_page_personel WHERE AD_SOYAD=?",(ad,))
         for i in a:


             if (i[1] == ad):

                 context = {"liste": liste, "x":"zaam"}
                 c.execute(
                     "INSERT INTO admin_page_donanım_dbs (TUR,MARKA,MODEL,SERI_NO,DURUM,LOKASYON,EVENT_id) VALUES (?,?,?,?,?,?,?) ",
                     (tür, marka, model, seri_no, lokasyon, durum, i[0]))
                 break
     conn.commit()

     c.close()

     return render(request, "show.html", context)



def mail(request):
    return render(request, "mail.html")


def sended(request):
    val1 = request.POST["mail"]
    val2 = request.POST["bas"]

    send_mail(val2,val1,"byteh84@gmail.com",["hinepa@royalweb.email"],
              fail_silently=False)
    return render(request, "sended.html")


def char(request):
    #liste=personel.objects.values('DEPARTMAN').annotate(dcount=Count('DEPARTMAN'))
  #  liste=personel.objects.all()

    lap=0
    mon=0
    yazıcı=0
    a=0
    diğer = 0
    everest=0
    hp=0
    no=0
    asus=0
    liste = donanım_dbs.objects.all()



    for i in liste:
        if (i.TUR).upper() == ("DizUstU Bilgisayar (Laptop)").upper():
            lap = lap+1

        elif (i.TUR).upper() == ("Yazıcı").upper():
            yazıcı = yazıcı+1

        elif (i.TUR).upper() == ("MonitOr").upper():
            mon = mon+1
        else:
            diğer=diğer+1

    for i in liste:

        if (i.MARKA).upper()==("HP&Compaq").upper():
            everest=everest+1
        elif (i.MARKA).upper()=="HP":
            hp = hp + 1
        elif (i.MARKA).upper() == ('UTAX').upper():
            asus = asus + 1
        else:
            no=no+1

    huk=0
    sat=44
    el=43
    notu=0
    x=""
    a=0
    for i in liste:
        if a==2:
            break
        if (i.EVENT.DEPARTMAN).upper()==("HUKUK MUSAViRLiGi").upper():
            huk=huk+1

        elif  (i.EVENT.DEPARTMAN).upper()=="SATiN ALMA VE TiCARET SEFLiGi":
            sat = sat + 1
        elif  (i.EVENT.DEPARTMAN).upper() == ('ELEKTRONiK VE BiLGi SiSTEMLERi GRUP BAS MUHENDiSLiGi').upper():
            el = el + 1
        else:
            notu=notu+1
            x=i.EVENT.DEPARTMAN

        a=a+1
    datam=[a,lap,mon,yazıcı,diğer]
    datamAd=["=","DİZ. LAPTOP","MONİTOR","YAZICI","DİĞER"]

    datam_two = [a, everest, hp, asus, no]
    datamAd_two = ["=", "HP&Compaq", "HP", "UTAX", "DİĞER"]

    datam_three = [a, huk, sat, el, notu]
    datamAd_three = ["=", "HUKUK MUSAViRLiGi", "SATiN ALMA VE TiCARET SEFLiGi", "ELEKTRONiK VE BiLGi SiSTEMLERi GRUP BAS MUHENDiSLiGi", "DİĞER"]

    return render(request, "char.html",{"datam":datam,"datamAd":datamAd,"datam_two":datam_two,"datamAd_two":datamAd_two,"datam_three":datam_three,"datamAD_three":datamAd_three,"x":x})


def demir(request):
    return render(request, "main_2.html")


def dosya(request):
    return render(request, "dosya.html")

def result(request):
    #val1 = request.GET["myFile"]


    val1=request.GET["file"]
    val1="C:\\Users\\selah\\Desktop\\"+ val1

    id_personel=1
    id_donanım=1
    f = open(val1, 'r', encoding='unicode_escape')
    for line in f:


        line = line.split(';')

        conn = sqlite3.connect('db.sqlite3')
        c = conn.cursor()

        liste = donanım_dbs.objects.all()
        a=0
        for i in liste:
            if i.EVENT.AD_SOYAD==line[4]:
                c.execute(
                    "INSERT INTO admin_page_donanım_dbs (id,TUR,MARKA,MODEL,SERI_NO,DURUM,LOKASYON,EVENT_id) VALUES (?,?,?,?,?,?,?,?) ",
                    (id_donanım, line[0], line[1], line[2], line[3], line[7], line[6],i.EVENT_id))
                a=1
                break

        if a!=1:

            c.execute("INSERT INTO admin_page_donanım_dbs (id,TUR,MARKA,MODEL,SERI_NO,DURUM,LOKASYON,EVENT_id) VALUES (?,?,?,?,?,?,?,?) ",
                      (id_donanım, line[0], line[1], line[2], line[3], line[7], line[6], id_personel))
            c.execute("INSERT INTO admin_page_personel (id, AD_SOYAD,DEPARTMAN) VALUES (?,?,?) ", ( id_personel,line[4],line[5]))
        conn.commit()

        c.close()
        id_personel=id_personel+1
        id_donanım=id_donanım+1

    f.close()

    context = {"a": "DATABESE YÜKLEME BAŞARILI OLDU CANIM"}
    return render(request, "result.html",context)



def malzeme(request):
    liste = donanım_dbs.objects.all()


    monitor=0
    masustu=0
    Yazici=0
    top=0
    a=0
    di=0
    diz=0
    tar=0

    Tmonitor = 0
    Tmasustu =0
    TYazici = 0
    Tsik = 0
    Tdi =0
    Tdiz = 0
    Ttar = 10
    a=0
    for i in liste:

        if (i.DURUM)==("VAR"):
            top = top + 1
            if (i.TUR).upper() == ("Yazıcı").upper():
                Yazici=Yazici+1
            elif (i.TUR).upper() == ("MasaUstU Bilgisayar (PC)").upper():
                masustu=masustu+1
            elif (i.TUR).upper() == ("MonitOr").upper():
                monitor=monitor+1
            elif (i.TUR).upper() == ("DizUstU Bilgisayar (Laptop)").upper():
                diz = diz + 1
            elif (i.TUR).upper() == ("Tarayici").upper():
                tar = tar + 1
            else:
                di=di+1
        if (i.DURUM).strip() == ("TAMİRDE"):
            Tsik = Tsik + 1
            if (i.TUR).upper() == ("Yazıcı").upper():
                TYazici = TYazici + 1
            elif (i.TUR).upper() == ("MasaUstU Bilgisayar (PC)").upper():
                Tmasustu = Tmasustu + 1
            elif (i.TUR).upper() == ("MonitOr").upper():
               Tmonitor = Tmonitor + 1
            elif (i.TUR).upper() == ("DizUstU Bilgisayar (Laptop)").upper():
                Tdiz = Tdiz + 1
            elif (i.TUR).upper() == ("Tarayici").upper():
                Ttar = Ttar + 1
            else:
                Tdi = Tdi + 1

        a=i.DURUM
    print(a+"-"+a)
    saglam = [monitor,masustu,Yazici,diz,tar,di,top]
    saglamAd = ["MONİTOR", "MasaUstU Bilgisayar (PC)", "Yazıcı","DİZ PC","TARAYICI","DİĞER","TOPLAM"]

    tamir = [Tmonitor, Tmasustu, TYazici,  Tdiz, Ttar, Tdi,Tsik]
    tamirAd = ["MONİTOR", "MasaUstU Bilgisayar (PC)", "Yazıcı","DİZ PC", "TARAYICI", "DİĞER", "TOPLAM"]


    return render(request, "malzeme.html",{"saglam":saglam,"saglamAd":saglamAd,"tam":tamir,"tamAd":tamirAd,"liste":liste})

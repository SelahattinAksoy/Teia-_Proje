from django.db import models

# Create your models here.
##############################modeli temizle



class arızaKaydı(models.Model):
    TUR = models.CharField(max_length=100)
    MARKA = models.CharField(max_length=100)
    MODEL = models.CharField(max_length=100)
    SERI_NO = models.CharField(max_length=100)
    ARIZA = models.CharField(max_length=100)
    ARIZA_TARIH=models.DateField()



class bozuk(models.Model):
    TUR = models.CharField(max_length=100)
    MARKA = models.CharField(max_length=100)
    MODEL = models.CharField(max_length=100)
    SERI_NO = models.CharField(max_length=100)
    DURUM = models.CharField(max_length=100)

class sifre(models.Model):
    KULLANICI=models.CharField(max_length=100)
    SİFRE=models.CharField(max_length=100)


class personel(models.Model):
    AD_SOYAD=models.CharField(max_length=100)
    DEPARTMAN = models.CharField(max_length=100)


    def __str__(self):
        return self.AD_SOYAD+ " "+self.DEPARTMAN

class depo(models.Model):
    TUR = models.CharField(max_length=100)
    MARKA = models.CharField(max_length=100)
    MODEL = models.CharField(max_length=100)
    SERI_NO = models.CharField(max_length=100)
    DURUM = models.CharField(max_length=100)


class donanım_dbs(models.Model):

    EVENT=models.ForeignKey(personel,on_delete=models.CASCADE)
    TUR = models.CharField(max_length=100)
    MARKA = models.CharField(max_length=100)
    MODEL = models.CharField(max_length=100)
    SERI_NO = models.CharField(max_length=100)
    LOKASYON=models.CharField(max_length=100)
    DURUM = models.CharField(max_length=100)


    def __str__(self):
       return self.TUR
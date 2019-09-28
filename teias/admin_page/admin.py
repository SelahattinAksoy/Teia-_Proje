from django.contrib import admin

# Register your models here.
from .models import *
# Register your models here.
from django.contrib.auth.models import Group



admin.site.register(personel)
admin.site.register(donanım_dbs)
admin.site.register(sifre)
admin.site.register(depo)
admin.site.register(bozuk)

admin.site.site_header="TEİAŞ ADMİN PANELİ "
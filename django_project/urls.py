"""
URL configuration for django_project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
# import anasayfa
import anasayfa.views
import ogrenci.views
import ogretmen.views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/', anasayfa.views.anasayfa_f_en, name='home'),
    path('anasayfa/', anasayfa.views.anasayfa_f_tr, name='home'),
    path('', anasayfa.views.anasayfa, name='home'),
    path('ana/', anasayfa.views.anasayfa, name='home'),
    path('ogrenci/',ogrenci.views.ogrenci, name='home'),
    path('ogretmen/',ogretmen.views.ogretmen, name='ogretmen'),
    path('deneme/',anasayfa.views.deneme, name='deneme'),
    path('ogrencilistesi/',ogrenci.views.listeleme_f, name='ogrenciliste'),
#     # path('detay/<int:id>',ogrenci.views.detay, name='detay'),
#     path('ogrencilistegorunumu/',ogrenci.views.listeleme_f_listeSekli, name='ogrenciliste'),
    path('ogrenciekle/',ogrenci.views.ekle, name='ogrenciekleme'),
    path('ogrenciler/detay/<int:id>', ogrenci.views.detay, name='detay'),
    path('ogrencilistesi/',ogrenci.views.listeleme_f_listeSekli, name='ogrenciliste1'),
    path('ogrenciler/sil/<int:id>', ogrenci.views.sil, name='sil'),
    path('ogrenciler/guncelle/<int:id>', ogrenci.views.guncelle, name='guncelle'),
]
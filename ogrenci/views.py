from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.template import loader
# Create your views here.


def ogrenci_f(request):
  return HttpResponse("Öğrenci sayfasına hoş geldiniz.")

def ogrenci(request):
  xx = loader.get_template("ogrenci.html")
  return HttpResponse(xx.render())


def listeleme(request):
  return HttpResponse(loader.get_template("ogrenci.html").render())

from ogrenci.models import Talebe

# def listeleme_f(request):
#   ogrenciliste = Talebe.objects.all()
#   gidecekSayfa = loader.get_template("ogrenciler.html")
#   gidecekBilgi {"transferListe": gelenListe}
#   # print(gidecekBilgi["transferliste"])
#   return
# HttpResponse(gidecekSayfa.render(gidecekBilgi, request))
def listeleme_f1(request):
    gelenListe = Talebe.objects.all()
    gidecekSayfa = loader.get_template("ogrenciler.html")
    gidecekBilgi = {
        'transferliste': gelenListe,
    }
    # print(gidecekBilgi["transferliste"])
    return HttpResponse(gidecekSayfa.render(gidecekBilgi, request))

def listeleme_f(request):
    ogrenciliste = Talebe.objects.all()
    template = loader.get_template('ogrenciler.html')
    context ={
        'ogrenciliste1' : ogrenciliste,
    }
    return HttpResponse(template.render(context, request))

def listeleme_f_listeSekli(request):
    ogrenciliste = Talebe.objects.all()
    template = loader.get_template('ogrenciler_list.html')
    context = {
        'ogrenciliste1': ogrenciliste,
    }
    return HttpResponse(template.render(context, request))

from django import forms
from .models import Talebe


class ogrForm(forms.ModelForm):
    class Meta:
        model = Talebe
        fields = ['TC', 'AdiSoyadi', 'Aciklama','sinif']  
# Kullanmak istediğiniz alanları buraya ekleyin


def ekle(request):
    if request.method == 'POST':
        form = ogrForm(request.POST)
        if form.is_valid():
            # Form verileri işleme
            form.save()  # Veritabanına kaydetme
            # return redirect('ogrenciler')  #url name
    else:
        form = ogrForm()
    return render(request, 'ekle.html', {'form': form})

# def detay(request, id):
#   item = Talebe.objects.get(id=id)
#   template = loader.get_template('detay.html')
#   context = {
#     'item': item,
#   }
#   return HttpResponse(template.render(context, request))

def detay(request, id):
    item = Talebe.objects.get(id=id)
    ogrenciliste = Talebe.objects.all()
    gonderilen_veri = {
        'ogrenciliste1': ogrenciliste,
        'item': item,
      }
    template = loader.get_template('detay.html')

    return HttpResponse(template.render(gonderilen_veri, request))

def sil (request, id):
    item = Talebe.objects.get(id=id)
    item.delete()
    return redirect('ogrenciliste')


def guncelle(request, id):
    # ogrenci = get_object_or_404(Talebe, id=id)
    ogrenci = Talebe.objects.get(id=id)
   

    if request.method == 'POST':
        form = ogrForm(request.POST, instance=ogrenci)
        if form.is_valid():
            # Form verileri işleme
            form.save()  # Veritab. kaydetme
            return redirect('ogrenciliste') #url name
    else:
        form = ogrForm(instance=ogrenci) 
        ogrenciliste = Talebe.objects.all()
        gonderilen_veri = {
            'ogrenciliste1': ogrenciliste,
            'form': form,
        }
    return render(request, 'ekle.html', gonderilen_veri) 


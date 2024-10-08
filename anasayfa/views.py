from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def anasayfa_f_tr(request):
    return HttpResponse("Web sitesine hoş geldiniz.")

def anasayfa_f_en(request):
    return HttpResponse("Welcome my website.")
    
from django.template import loader

def anasayfa(request):
  giden_sayfa = loader.get_template('ana.html')
  return HttpResponse(giden_sayfa.render())


def deneme(request):
   return HttpResponse(loader.get_template('deneme.html').render())
    

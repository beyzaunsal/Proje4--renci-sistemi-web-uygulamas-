from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
# Create your views here.


def ogretmen_f(request):
  return HttpResponse("Öğretmen sayfasına hoş geldiniz.")

def ogretmen(request):
  yy= loader.get_template("ogretmen.html")
  return HttpResponse(yy.render())


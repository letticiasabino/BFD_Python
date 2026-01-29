from django.shortcuts import render
from django.http import HttpResponse

def home(request):
  return HttpResponse("Bem-vindo a página inicial da Minha Empresa!")

def servicos(request):
  return HttpResponse("Conheça nossas soluções")

def fale_conosco(request):
  return HttpResponse("Entre em contato conosco: Whasapp: (21) 99999-9999")


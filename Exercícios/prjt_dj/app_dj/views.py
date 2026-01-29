from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse

#A função a seguir irá lidar com a requisição para o index.
def index(request):
    #A View recebe um objeto HttpRequest (request)
    #E deve retornar um objeto HttpResponse
    return HttpResponse("Olá, mundo. Você está no index do meu segundo App Django.")
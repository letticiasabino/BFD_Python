from django.shortcuts import render, redirect
from .models import Pessoa

# Create your views here.

def formulario(request):
  if request.method == 'POST':
    Pessoa.objects.create(
      nome=request.POST['nome'],
      email=request.POST['email'],
      idade=request.POST['idade'],
      telefone=request.POST['telefone'],
      profissao=request.POST['profissao'],
      mensagem=request.POST['mensagem']
                          )
    return redirect('formulario')
  return render(request, 'forms/formulario.html')
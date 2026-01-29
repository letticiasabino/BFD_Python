from django.shortcuts import render
from django.http import HttpResponse
from .forms import CandidatoForm

# Create your views here.
def cadastro_candidato(request):
  form = CandidatoForm()

  # Se o usuário clicou no botão "Enviar" (POST)
  if request.method == 'POST':
    form = CandidatoForm(request.POST) # Pega os dados preenchidos
    if form.is_valid():
      # Aqui salva no banco ou mandaria um e-mail
      # Mensagem de Sucesso
      return HttpResponse ("<h1>Inscrição realizada com sucesso!</h1>")
    
  # Se o usuário abrir só a página do GET
  return render(request, 'index.html', {'form': form})
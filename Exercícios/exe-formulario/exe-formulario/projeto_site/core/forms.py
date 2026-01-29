from django import forms

class CandidatoForm(forms.Form):
  nome_completo = forms.CharField(label='Nome Completo', max_length=100)

  email = forms.EmailField(label='E-mail para Contato')

  idade = forms.IntegerField(label='Sua Idade', min_value=0, max_value=120)

  data_nascimento = forms.DateField(label="Data de Nascimento", widget=forms.DateInput(attrs={'type': 'date'}))

  AREAS_CHOICES = [
    ('ti', 'Tecnologia da Informação'),
    ('adm', 'Administração'),
    ('rh', 'Recursos Humanos'),
    ('mkt', 'Marketing'),
  ]

  area_interesse = forms.ChoiceField(choices=AREAS_CHOICES, label="Área de Interesse")

  resumo_profissional = forms.CharField(label="Resumo Profissional", widget=forms.Textarea(attrs={'rows': 3}))

  aceita_remoto = forms.BooleanField(label="Tenho disponibilidade para trabalhar remoto.", required=False)

  mensagem = forms.CharField(label='Informação Adicional', widget=forms.Textarea(attrs={'rows': 3}))
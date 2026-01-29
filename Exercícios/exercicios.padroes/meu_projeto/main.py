from processadores.csv import ProcessadorCSV
from processadores.txt import ProcessadorTXT

from notificacoes.email import enviar_email
from notificacoes.sms import sms
from notificacoes.whatsapp import whatsapp

from logistica.terrestre import LogisticaTerrestre
from logistica.maritima import LogisticaMaritima


print("\n=== TESTE TEMPLATE METHOD ===")
csv = ProcessadorCSV()
print(csv.processar("dados.csv"))

txt = ProcessadorTXT()
print(txt.processar("dados.txt"))


print("\n=== TESTE DECORATORS ===")
enviar_sms = sms(enviar_email)
enviar_sms("cliente@teste.com")

enviar_zap = whatsapp(enviar_email)
enviar_zap("cliente@teste.com")


print("\n=== TESTE FACTORY METHOD ===")
terrestre = LogisticaTerrestre()
terrestre.planejar_entrega()

maritima = LogisticaMaritima()
maritima.planejar_entrega()
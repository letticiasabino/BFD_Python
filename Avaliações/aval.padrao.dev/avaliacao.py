from abc import ABC, abstractmethod

class Notificador(ABC):
  def postar_aviso(self, mensagem):
    mensagem_formatada = mensagem + " | Ass: Bolsa Futuro Digital" # Adiciona a assinatura padrão

    self.enviar(mensagem_formatada) # Chama o método enviar (definido nas subclasses)

  @abstractmethod
  def enviar(self, texto):
    pass

class NotificadorEmail(Notificador):
  def enviar(self, texto):
    print(f"Enviando Email: {texto}")

class NotificadorZap(Notificador):

    def enviar(self, texto):
        print(f"Enviando Whatsapp: {texto}")

# Decorator

def auditoria(func):
   def wrapper(*args, **kwargs):
      print("--- Início do Processo ---")
      resultado = func(*args, **kwargs)
      print("--- Fim do Processo ---")
      return resultado
   return wrapper

@auditoria
def cliente_enviar(notificador, mensagem):
   notificador.postar_aviso(mensagem)


# Teste

if __name__ == "__main__":
   print("\n### Teste com NotificadorEmail ###")
   email = NotificadorEmail()
   cliente_enviar(email, "Sua atividade está disponível no portal.")

   print("\n### Teste com NotificadorZap ###")
   zap = NotificadorZap()
   cliente_enviar(zap, "Lembrete: aula ao vivo hoje às 19h.")
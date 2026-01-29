from abc import ABC, abstractmethod

# ==========================================
# 1. PADRÃO TEMPLATE METHOD
# ==========================================

class Notificador(ABC):

    def postar_aviso(self, mensagem):
        # 1. Adiciona a assinatura padrão
        mensagem_formatada = mensagem + " | Ass: Bolsa Futuro Digital"

        # 2. Chama o método enviar (definido nas subclasses)
        self.enviar(mensagem_formatada)

    @abstractmethod
    def enviar(self, texto):
        pass


class NotificadorEmail(Notificador):

    def enviar(self, texto):
        print(f"Enviando E-MAIL: {texto}")


class NotificadorZap(Notificador):

    def enviar(self, texto):
        print(f"Enviando ZAP: {texto}")


# ==========================================
# 2. PADRÃO DECORATOR
# ==========================================

def auditoria(func):
    def wrapper(*args, **kwargs):
        print("--- Início do Processo ---")
        resultado = func(*args, **kwargs)
        print("--- Fim do Processo ---")
        return resultado
    return wrapper


# ==========================================
# 3. CÓDIGO CLIENTE
# ==========================================

@auditoria
def cliente_enviar(notificador, mensagem):
    notificador.postar_aviso(mensagem)


# ==========================================
# TESTES (como pedido pela avaliação)
# ==========================================

if __name__ == "__main__":

    print("\n### Teste com NotificadorEmail ###")
    email = NotificadorEmail()
    cliente_enviar(email, "Sua atividade está disponível no portal.")

    print("\n### Teste com NotificadorZap ###")
    zap = NotificadorZap()
    cliente_enviar(zap, "Lembrete: aula ao vivo hoje às 19h.")

def sms(func):
  def wrapper(destinatario):
    print("Enviando SMS...")
    func(destinatario)
  return wrapper
def whatsapp(func):
  def wrapper(destinatario):
    print("Enviando Whatsapp...")
    func(destinatario)
  return wrapper
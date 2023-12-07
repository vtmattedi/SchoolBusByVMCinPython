from Helpers import SafeInput

class Endereco:
  def __init__(self, rua="", numero=None, complemento="", bairro=""):
      self.rua = rua
      self.numero = numero
      self.complemento = complemento
      self.bairro = bairro

  def request(self):
      self.rua = input("Rua: ")
      self.numero = SafeInput.get_int("Numero[inteiro]: ")
      self.complemento = input("Complemento: ")
      self.bairro = input("Bairro: ")
  #permite o uso de print(Endereco)
  def __str__(self) -> str:
    return f"Endereço: {self.rua}, {self.numero}, {self.complemento}, {self.bairro}."



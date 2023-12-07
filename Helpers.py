from datetime import datetime

#classe com metodos estaticos para tratamento de input com formato especifico.
class SafeInput:
  @staticmethod
  def get_int(prompt):
    input_str = input(prompt)
    try: 
      rtr = int(input_str)
    except ValueError:
      print("O input tem que ser um inteiro.")
      rtr = SafeInput.get_int(prompt)
    return rtr
    
  @staticmethod
  def get_float(prompt):
    input_str = input(prompt)
    try: 
      rtr = float(input_str)
    except ValueError:
      print("O input tem que ser um float.")
      rtr = SafeInput.get_int(prompt)
    return rtr
    
  @staticmethod
  def get_date(date_str):
    try:
      rtr = datetime.strptime(date_str, "%d/%m/%Y").date()
    except ValueError:
      print("Data inválida. Tente novamente.")
      date_str = input("Data de Nascimento [formato dia/mes/ano]: ")
      rtr = SafeInput.get_date(date_str)
    return rtr
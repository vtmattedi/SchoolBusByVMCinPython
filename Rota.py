class PontoDeParada:
  #variaveis separadas para manter IDs unicas e o numero de pontos de parada em memoria
  __count = 0
  __nextId = 0

  def __init__(self, nome="", latitude=0.0, longitude=0.0):
      self.nome = nome
      self.latitude = latitude
      self.longitude = longitude
      self.id = PontoDeParada.__nextId
      self.alunos = []
      PontoDeParada.__nextId += 1
      PontoDeParada.__count += 1

  def __del__(self):
      PontoDeParada.__count -= 1

  #"overload" para print(Ponto de parafa)
  def __str__(self) -> str:
    return f"Ponto de parada: {self.nome} latitude: {self.latitude} longitude: {self.longitude} ID: {self.id}"

  def get_id(self):
    return self.id
  def reciprocate(self, novoAluno, added):
    #esse aluno adicionou este ponto de parada
      if added:
          if novoAluno not in self.alunos:
              self.alunos.append(novoAluno)
      #esse aluno removeu este ponto de parada
      else:
          if novoAluno in self.alunos:
              self.alunos.remove(novoAluno)

class Rota:
  __count = 0
  __nextId = 0

  def __init__(self, pontos_de_parada=None):
      if pontos_de_parada is None:
        pontos_de_parada = []
      self.id = Rota.__nextId
      self.pontos = pontos_de_parada
      Rota.__nextId += 1
      Rota.__count += 1

  def __del__(self):
      Rota.__count -= 1

  def add_ponto(self, ponto):
      self.pontos.append(ponto)

  def calcular_demanda(self):
      total_alunos = sum(len(ponto.getAlunos()) for ponto in self.pontos)
      print(f"Demanda da Rota [{self.id}] é de {total_alunos} alunos, em um total de {len(self.pontos)} paradas.")

  @staticmethod
  def numero_de_rotas():
      print("Numero de rotas:", Rota.__count)

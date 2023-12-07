#Modulo com a classe base de Pessoa e suas derivações
from abc import *
from Helpers import SafeInput
from endereco import Endereco
from Rota import PontoDeParada

class Pessoa:

  def __init__(self, nome_oficial, cpf_cnpj, endereco, telefone):
    self.__nome_oficial = nome_oficial
    self.__cpf_cnpj = cpf_cnpj
    self.endereco = endereco
    self.telefone = telefone

  @property
  def getNomeOficial(self):
    return self.__nome_oficial

  def setNomeOficial(self, value):
     self.__nome_oficial = value

  @property
  def getCpfCnpj(self):
    return self.__cpf_cnpj

  def setCpfCnpj(self, value):
     self.__cpf_cnpj = value

  #metodo usado por cada classe que herda Pessoa para requerer os dados nescessarios ao usuario.
  @abstractmethod
  def request(self):
    pass

  @abstractmethod
  def apresentarDados(self):
    pass

  def verificarTipo(self):
    #poderia usar o isintance(obj, type) do pyhton, mas vou retornar o nome da classe ao inves disso pois o tipo de retorno vai ser string de qualquer forma e dessa forma é menos elegante porém mais prática
    return type(self).__name__

#Classes base Pessoa Fisica e Pessoa Juridica
class PessoaFisica(Pessoa):
  def __init__(self,
               nome_oficial="",
               cpf_cnpj="",
               endereco="",
               telefone="",
               nome_social="",
               mae="",
               pai="",
               naturalidade="",
               data_nascimento=""):
    super().__init__(nome_oficial, cpf_cnpj, endereco, telefone)
    self.nome_social = nome_social
    self.mae = mae
    self.pai = pai
    self.naturalidade = naturalidade
    self.data_nascimento = data_nascimento

  def request(self):
    self.nome_civil = input("Nome Civil: ")
    self.nome = input(
        "Nome Social (deixar em branco caso não queria declarar): ")
    if self.nome_social is None or self.nome_social == "":
      self.nome_social = self.nome_civil  # Preenche o nome social com o nome civil por padrão
    self.mae = input("Nome da Mãe: ")
    self.pai = input("Nome do Pai: ")
    self.naturalidade = input("Naturalidade: ")
    self.cpf_cnpj = input("CPF: ")
    data_nascimento_str = input("Data de Nascimento [formato dia/mes/ano]: ")
    self.dataNascimento = SafeInput.get_date(data_nascimento_str)

  #por  definição do exercico incremental V
  def getCPF(self):
    return super().getCpfCnpj

  def getNomeCivil(self):
    return super().getNomeOficial

class PessoaJuridica(Pessoa):
#Do Exercico incremental V temos: 'Em PessoaJuridica implemente o método getNomeFantasia que retorna o nome nome oficial da pessoa.', portanto para pessoa Juridica, Nome Fantasia é o mesmo que o nome_oficial.
  def __init__(self,
               nome_oficial="",
               cnpj="",
               endereco="",
               telefone="",
               num_funcionario=0):
    super().__init__(nome_oficial, cnpj, endereco, telefone)
    self.num_funcionario = num_funcionario

  #por definição do exercico incremental V
  
  def getCNPJ(self):
    return super().getCpfCnpj

  
  def getNomeFantasia(self):
    return super().getNomeOficial

  def request(self):
    self.nome = input("Nome Oficial: ")
    self.num_funcionario = SafeInput.get_int(
        "Numero de funcionarios [inteiro]: ")
    self.cpf_cnpj = input("CNPJ: ")
    self.telefone = input("Telefone: ")
    print("Endereço: ")
    self.endereco = Endereco()
    self.endereco.request()

#Classes que herdam PessoaJuridica
class Fornecedor(PessoaJuridica):
  def __init__(self,
               nome_oficial="",
               cpf="",
               endereco="",
               telefone="",
               num_funcionario=0):
    super().__init__(nome_oficial, cpf, endereco, telefone,   num_funcionario)
    self.contratos = []

  def reciprocrate(self, contrato, Added):
    if Added:
      if contrato not in self.contratos:
         self.contratos.append(contrato)
    else:
      if contrato in self.contratos:
         self.contratos.remove(contrato)
  
  def add_contrato(self, contrato):
    if(type(contrato).__name__ != "Contrato"):
      print(type(contrato))
      print("Tipo de contrato inválido, passa um objeto Contrato")
      return False
    self.reciprocrate(contrato, True) #o mesmo que adicionar
    contrato.reciprocate_fornecedor(self)

  def request(self):
    self.setNomeOficial(input("Nome Fantasia: "))
    self.num_funcionario = SafeInput.get_int(
      "Numero de funcionarios [inteiro]: ")
    self.cpf_cnpj = input("CNPJ: ")
    print("Endereço do Forneçedor: ")
    self.endereco = Endereco()
    self.endereco.request()

  def apresentarDados(self):
    print(f"Nome Oficial: {self.getNomeFantasia()}")
    print(f"CNPJ: {self.getCNPJ()}")
    print(f"Telefone: {self.telefone}")
    print("Endereço: {",self.endereco,"}")
    print(f"Número de Funcionários: {self.num_funcionario}")
    print("Contratos: Matriculados::")
    for contrato in self.contratos:
        print(f"  - Contrato No.: {contrato.num_contrato}")
 
#Classe Escola
class Escola(PessoaJuridica):
  def __init__(self,
             nome_oficial="",
             cnpj="",
             endereco="",
             telefone="",         
             num_funcionario=0):
    super().__init__(nome_oficial, cnpj, endereco, telefone,num_funcionario)
    self.alunos = []

  def matricular_aluno(self):
    new_aluno = Aluno()
    new_aluno.request()
    self.alunos.append(new_aluno)
    return new_aluno

  def exibir_todos(self):
    print("Nome da Escola: ", self.getNomeOficial)
    print("lista de alunos: ")
    for aluno in self.alunos:
      print(aluno)
  
  def request(self):
    self.setNomeOficial(input("Nome Fantasia: "))
    self.num_funcionario = SafeInput.get_int(
        "Numero de funcionarios [inteiro]: ")
    self.cpf_cnpj = input("CNPJ: ")
    print("Endereço da Escola: ")
    self.endereco = Endereco()
    self.endereco.request()

  def apresentarDados(self):
    print(f"Nome Oficial: {self.getNomeFantasia()}")
    print(f"CNPJ: {self.getCNPJ()}")
    print(f"Telefone: {self.telefone}")
    print("Endereço: {",self.endereco,"}")
    print(f"Número de Funcionários: {self.num_funcionario}")
    print("Alunos Matriculados::")
    for aluno in self.alunos:
        print(f"  - {aluno.getNomeOficial}")
    
#Classes que herdam PessoaFisica

class Motorista(PessoaFisica):

  def __init__(self,nome_oficial="",cpf_cnpj="",endereco="",telefone="",nome_social="",mae="",
               pai="",naturalidade="",data_nascimento="",num_habilitacao = 0,
               cat_habilitacao = "", tipo = 0
               ,num_contrato=None):
    super().__init__(nome_oficial,cpf_cnpj,endereco,telefone,
                     nome_social,mae,pai,naturalidade,data_nascimento)
    self.num_habilitacao = num_habilitacao
    self.cat_habilitacao = cat_habilitacao
    self.tipo = tipo
    self.num_contrato = num_contrato
    self.contratos = []

  def is_terceirizado(self):
    return self.tipo == 1

  def reciprocate(self, contrato):
    self.add_contrato(contrato)

  def add_contrato(self, contrato):
    if contrato not in self.contratos:
      self.contratos.append(contrato)

  def set_num_contrato(self, num_contrato):
    if self.tipo == 0:
      print("Método inválido. Motorista Servidor")
    else:
      self.num_contrato = num_contrato
      
  def apresentarDados(self):
    print("Dados do Motorista:")
    print(f"Nome Civil: {self.getNomeOficial}")
    print(f"Nome Social: {self.nome}")
    print(f"CPF: {self.getCPF}")
    print(f"Data de Nascimento: {self.data_nascimento}")
    print(f"Número da Habilitação: {self.num_habilitacao}")
    print(f"Categoria da Habilitação: {self.cat_habilitacao}")
    print(f"Tipo: {'Terceirizado' if self.is_terceirizado() else 'Servidor'}")
    if self.num_contrato:
        print(f"Número do Contrato: {self.num_contrato}")
    print("Contratos Associados:")
    for contrato in self.contratos:
       print(f"  - Contrato No.: {contrato.num_contrato}")

    def request(self):
      self.nome_civil = input("Nome Civil: ")
      self.nome = input(
          "Nome Social (deixar em branco caso não queria declarar): ")
      if self.nome_social is None or self.nome_social == "":
        self.nome_social = self.nome_civil  # Preenche o nome social com o nome civil por padrão
      self.mae = input("Nome da Mãe: ")
      self.pai = input("Nome do Pai: ")
      self.naturalidade = input("Naturalidade: ")
      self.cpf_cnpj = input("CPF: ")
      data_nascimento_str = input("Data de Nascimento [formato dia/mes/ano]: ")
      self.dataNascimento = SafeInput.get_date(data_nascimento_str)
      self.num_habilitacao = SafeInput.get_int("Numero da Habilitação[inteiro]: ")
      self.cat_habilitacao = input("Categoria da Habilitação: ")
      _terceirizado = SafeInput.get_int("Terceirizado:1 ou Servidor:0 (padrão: 0)[inteiro]: ")
      if _terceirizado == 1:
        self.tipo = 1
        self.num_contrato = SafeInput.get_int("Numero do Contrato: ")
      else:
        self.tipo = 0

class Aluno(PessoaFisica):
  def __init__(self,
             nome_oficial="",
             cpf_cnpj="",
             endereco="",
             telefone="",
             nome_social="",
             mae="",
             pai="",
             naturalidade="",
             data_nascimento="",
             matricula = 0,
             serie = 0):
    super().__init__(nome_oficial,
       cpf_cnpj,
       endereco,
       telefone,
       nome_social,
       mae,
       pai,
       naturalidade,
       data_nascimento)
    self.matricula = matricula
    self.serie = serie
    self.__ponto_de_parada = None

  def request(self):
    self.nome_civil = input("Nome Civil: ")
    self.nome = input(
        "Nome Social (deixar em branco caso não queria declarar): ")
    if self.nome_social is None or self.nome_social == "":
      self.nome_social = self.nome_civil  # Preenche o nome social com o nome civil por padrão
    self.mae = input("Nome da Mãe: ")
    self.pai = input("Nome do Pai: ")
    self.naturalidade = input("Naturalidade: ")
    self.setCpfCnpj(input("CPF: "))
    data_nascimento_str = input("Data de Nascimento [formato dia/mes/ano]: ")
    self.dataNascimento = SafeInput.get_date(data_nascimento_str)
    self.matricula = SafeInput.get_int("Matrícula: ")
    self.serie = SafeInput.get_int("Serie:")

  #"overload" para print(Aluno)
  def __str__(self) -> str:
    return (f"Nome: {self.getNomeOficial} CPF: {self.getCpfCnpj} Matricula: {self.matricula} Serie: {self.serie} Naturalidade: {self.naturalidade} Pai: {self.pai} Mãe: {self.mae}")

  def set_ponto_de_parada(self, value):
    if (type(value).__name__ != "PontoDeParada"):
      print("tipo invalido, favor passar um objeto do tipo PontoDeParada")
      return False
    if self.__ponto_de_parada:
      #desassocia este objeto com do ponto de parada anterior
      self.__ponto_de_parada.reciprocate(self, False)
    self.__ponto_de_parada = value
     #associa este objeto com o ponto de parada no objeto do ponto de parada
    value.reciprocate(self, True)
    return True

  @property
  def get_ponto_de_parada(self):
    return self.__ponto_de_parada

  def apresentarDados(self):
    print("Dados do Aluno:")
    print(f"Nome Social: {self.nome_social}")
    print(f"Nome Civil: {self.getNomeOficial}")
    print(f"CPF: {self.getCpfCnpj}")
    print(f"Telefone: {self.telefone}")
    print(f"Data de Nascimento: {self.data_nascimento}")
    print(f"Nome da Mãe: {self.mae}")
    print(f"Nome do Pai: {self.pai}")
    print(f"Naturalidade: {self.naturalidade}")
    #endereço é printable pois foi declarado __str__ na classe.
    print("Endereço: {",self.endereco,"}")
    print(f"Serie: {self.serie}")
    print(f"Matricula: {self.matricula}")
    if (self.__ponto_de_parada):
      #ponto de parada tambem é printable pois foi declarado __str__ na classe.
      print("Ponto de Parada: {",self.__ponto_de_parada,"}")
    else:
      print("Ponto de Parada: Sem ponto de parada associado")
      


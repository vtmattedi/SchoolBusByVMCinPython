
class Veiculo:
    def __init__(self, placa, ano, modelo, capacidade, tipo, num_contrato=None):
        self.placa = placa
        self.ano = ano
        self.modelo = modelo
        self.capacidade = capacidade
        self.tipo = tipo
        self.num_contrato = num_contrato
        self.contrato = None

    def alugado(self):
        return self.tipo == 1

    def reciprocate(self, contrato):
        self.set_contrato(contrato)

    def set_contrato(self, contrato):
        if self.contrato:
            self.contrato.reciprocate(self, False)
        self.contrato = contrato
        contrato.reciprocate(self, True)




class Contrato:
    def __init__(self, num_contrato, data_inicio, data_fim, valor):
        self.num_contrato = num_contrato
        self.data_inicio = data_inicio
        self.data_fim = data_fim
        self.valor = valor
        self.veiculos = []
        self.motoristas = []
      #fornecedor não foi definido como lista no Incremental V. por tanto implementei como um contrato pode ter apenas um fornecedor
        self.fornecedor = None

    def add_veiculo(self, veiculo):
        if not veiculo.is_alugado():
            print("Veiculo não é alugado")
            return False
        elif veiculo in self.veiculos:
            print("Veiculo já existe no contrato")
            return False
        self.veiculos.append(veiculo)
        veiculo.reciprocate(self, True)
        return True

    def add_motorista(self, motorista):
        if not motorista.is_terceirizado():
            print("Motorista não é terceirizado")
            return False
        elif motorista in self.motoristas:
            print("Motorista já existe no contrato")
            return False
        self.motoristas.append(motorista)
        motorista.reciprocate(self, True)
        return True
    #garante coerencia entre os objetos de contrato e veiculo
    def reciprocate_veiculo(self, veiculo, added):
        if veiculo in self.veiculos and not added:
            self.veiculos.remove(veiculo)
        if veiculo not in self.veiculos and added:
            self.veiculos.append(veiculo)
   #garante coerencia entre os objetos de contrato e motorista
    def reciprocate_motorista(self, motorista, added):
        if motorista in self.motoristas and not added:
            self.motoristas.remove(motorista)
        if motorista not in self.motoristas and added:
            self.motoristas.append(motorista)
    #garante coerencia entre os objetos de contrato e fornecedor
    def reciprocate_fornecedor(self,fornecedor):
      self.fornecedor = fornecedor

    def add_fornecedor(self,pessoaJuridica):
      if (pessoaJuridica.verificarTipo() != "Fornecedor"):
        print("Objeto passado não é fornecedor.")
      else:
        #desassocia o fornecedor antigo ao contrato
        if(self.fornecedor): #se nào nulo
         self.fornecedor.reciprocate(self, False)
        self.fornecedor = pessoaJuridica
        #associa o fornecedor novo ao contrato
        self.fornecedor.reciprocate(self, True)
        
  


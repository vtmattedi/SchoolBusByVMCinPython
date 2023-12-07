# Author: Vitor Mattedi Carvalho. 
#   Project: Trabalho Final, Projeto incremental em python
#      Trabalho Final da materia POO, MATA 55 UFBA. 
 
from endereco import *  #importa Endereco e PersonalInfo
from Helpers import SafeInput  #importa SafeInput para tratar erros de entrada
from Contrato import *  #importa Motorista, Veiculo e Contrato
from Pessoa import *  #importa a classe Pessoa e todas suas heranças substituiu o antigo PersonalInfo
from Rota import *  #importa Rota e PontoDeParada

#comentar ou settar para falso para não rodar os testes
test = False
#Listas de objetos criados
rotas = []
pontos = []
escolas = []
alunos = []
motoristas = []
veiculos = []
contratos = []
fornecedores = []

#Para a parte V foi criada uma lista com a referencia de todos os objetos criados que herdam de pessoa.
pessoas = [] #lista de listas de pessoas
pessoas.append(escolas)
pessoas.append(alunos)
pessoas.append(motoristas)
pessoas.append(fornecedores)


def main():
    print("Bem vindo ao sistema SchoolBus by VMC")
    quit_program = False

    while not quit_program:
        menu()
        user_input = input()
        index = user_input.find(" ")

        if index > -1:
            command = user_input[:index]
            arg = user_input[index + 1:]
            handle_command(command, arg)
        elif user_input.lower() in ["quit", "q"]:
            quit_program = True
        elif user_input.lower() == "debug":
            # Implementar lógica para ligar/desligar o debugador, se necessário
            pass
        else:
            print(f"O input: '{user_input}', não foi reconhecido como um comando válido.")


#print do menu
def menu():
    print()
    print("------------------------------------------------------------------------------")
    print("Digite: criar [aluno|rota|escola|motorista|contrato|veiculo|ponto_de_parada]")
    print("     ou: listar [pontos_de_parada|rotas|pessoas]")
    print("     ou: calcular [id da rota]")
    print("     ou: relacionar_ponto [nome civil ou cpf do aluno]")
    print("     ou: relacionar_contrato [nome fantasia do fornecedor]")
    print("     ou: informacao [nome civil ou nome fantasia]")
    print("     ou: exibir [nome civil ou nome fantasia]")
    print("     ou: [quit|q] para sair, [debug] para ligar/desligar o debugador")
    print("------------------------------------------------------------------------------")

#Lidar com o comando desejado e os argumentos 
def handle_command(cmd, arg):
    #print(cmd,arg)
    if cmd == "criar":
      #criar escola
        if arg == "escola":
            nova_escola = Escola()
            nova_escola.request()
            escolas.append(nova_escola)
            print(f"Escola {nova_escola.getNomeOficial} criada.")
        #criar aluno
        elif arg == "aluno":
            #nao pode criar um aluno se nao houver escolar no sistema
            if not escolas:
                print("Não existem escolas no sistema. Crie uma escola antes de adicionar um aluno.")
                return

            index_escola = -1
            max_escolas = len(escolas)

            print("Escolha a escola do aluno pelo número:")
            for i, escola in enumerate(escolas):
                print(f" - [{i}]: {escola.getNomeOficial}")

            while index_escola < 0:
                index_escola = SafeInput.get_int("")
                if index_escola >= max_escolas:
                    index_escola = -1
                    print("Escola Invalida, escolha o número de uma das escolas listadas")


            aluno = escolas[index_escola].matricular_aluno()
          #se houver pontos de parada no sistema, já pode associar o aluno com um ponto de parada
            if pontos:
                response = input(f"Deseja relacionar '{aluno.setNomeOficial}' a um ponto de parada? [y/n] ")
                if response.lower() == "y":
                    print(f"Lista de pontos de parada disponíveis ({len(pontos)}):")
                    for i, ponto in enumerate(pontos):
                        print(f" - [{i}] nome: {ponto.nome}.")

                    ponto_index = int(input("Digite o índice do ponto de parada do aluno: "))

                    if 0 <= ponto_index < len(pontos):
                        if(aluno.set_ponto_de_parada(pontos[ponto_index])):
                          print("Ponto de parada relacionado com sucesso.")
                    else:
                        print(f"O índice '{ponto_index}' é inválido, aluno ainda não relacionado a nenhum ponto de parada.")
            alunos.append(aluno)
            print(f"Aluno {aluno.getNomeOficial} criado(a).")
        #criar Motorista
        elif arg == "motorista":
            mot = Motorista()
            mot.request()
            motoristas.append(mot)
        #criar veiculo
        elif arg == "veiculo":
            placa = input("Placa: ")
            modelo = input("Modelo: ")
            yr = SafeInput.get_int("Número do contrato: ")
            cap = SafeInput.get_int("Número do Capacidade: ")
            tipo = SafeInput.get_int("Tipo: [0 - Próprio, 1 - Alugado] [padrão: 0]")
            num_contrato = 0

            if tipo == 1:
                num_contrato = SafeInput.get_int("Número do contrato: ")
            if tipo == 1:
              car = Veiculo(placa, yr, modelo, cap, 1, num_contrato)  
            else:
              car = Veiculo(placa, yr, modelo, cap, 0)
            veiculos.append(car)
            print("Veículo adicionado.")
        #criar Contrato
        elif arg == "contrato": 
            start_date = SafeInput.get_date(input("Data do incio do contrato [dd/mm/aaaa]: "))
            end_date = SafeInput.get_date(input("Data do fim do contrato [dd/mm/aaaa]: "))
            val = SafeInput.get_float(input("Valor[float]: "))
            num_contrato = SafeInput.get_int(input("Número do contrato[inteiro]: "))
            contrato = Contrato(num_contrato, start_date, end_date, val)
            contratos.append(contrato)
            print("Contrato adicionado.")
          #se existirem fornecedores no sistema, pode associar o contrato criado a ele.
            if fornecedores:
                response = input("Deseja relacionar este contrato a um fornecedor?[y/n]")
                if response == "y":
                  print("Fornecedores disponiveis no sistema:")
                  for i, fornecedor in enumerate(fornecedores):
                    print(f" - [{i}] nome: {fornecedor.getNomeOficial}.")
                  index = SafeInput.get_int(input("Digite o índice do fornecedor que deseja selecionar: "))
                  if index >= len(fornecedores) or index < 0:
                    print("index inválido. contrato não relacionado a nenhum fornecedor neste momento.")
                  else:
                    if  contrato.add_fornecedor(fornecedores[index]):
                      print(f"Contrato relacionado ao fornecedor {fornecedores[index].getNomeOficial} com sucesso.")   
        #criar fornecdor     
        elif arg == "fornecedor": 
            fornecedor = Fornecedor()
            fornecedor.request()
            fornecedores.append(fornecedor)
            print("Fornecedor adicionado.")
        #criar Rota
        elif arg == "rota":
            if not pontos:
                print("Não existem pontos de parada no sistema. Crie pontos de parada antes de criar uma rota.")
                return

            print("Lista de pontos de parada disponíveis: ")
            for i, ponto in enumerate(pontos):
                print(f" - [{i}]: {ponto.nome}.")

            user_pontos = input("Digite a lista de pontos que deseja adicionar à nova rota, separados por ',' (índices inválidos são ignorados), exemplo: '1,3,10': ")
            splited = user_pontos.split(",")
            valid_pontos = []

            for current_split in splited:
                try:
                    current_ponto = int(current_split)
                    if 0 <= current_ponto < len(pontos):
                        if current_ponto not in valid_pontos:
                              valid_pontos.append(current_ponto)
                except ValueError:
                    pass

            rota = Rota()
            for ponto_index in valid_pontos:
                rota.add_ponto(pontos[ponto_index])

            print(f"Rota criada com {len(valid_pontos)} pontos.")
        #criar pontos de parada
        elif arg == "ponto_de_parada":
            name = input("Nome do ponto de parada: ")
            longi = SafeInput.get_float(input("Longitude: "))
            lati = SafeInput.get_float(input("Latitude: "))
            pontos.append(PontoDeParada(name, lati, longi))
            print(f"Ponto de parada '{name}' adicionado com sucesso.")
         #argumento invalido para comando de criar alguma coisa no sistema
        else:
            print(f"O argumento '{arg}' não foi reconhecido como válido. Tente 'criar ponto_de_parada'.")
    elif cmd == "listar":
      #lista as rotas cadastradas
        if arg == "rotas":
            print(f"Lista de rotas disponíveis ({len(rotas)}): ")
            for i, rota in enumerate(rotas):
                print(f" - [{i}] ID: {rota.get_id()}.")
      #lista os pontos de parada cadastrados
        elif arg == "pontos_de_parada":
            print(f"Lista de pontos de parada disponíveis ({len(pontos)}): ")
            for i, ponto in enumerate(pontos):
                 print(f" - [{i}] nome: {ponto.nome} ID: {ponto.get_id()}.")
      #lista os pontos de parada cadastrados
        elif arg == "pessoas":
            print(f"Lista de Pessoas Fisicas e Juridicas disponíveis no sistema : ")
            for list in pessoas:
                for i, pessoa in enumerate(list):
                 print(f" - [{i}] nome: {pessoa.getNomeOficial} tipo: {pessoa.verificarTipo()}")
      #argumento invalido para comando de listar alguma coisa no sistema
        else:
              print(f"O argumento '{arg}' não foi reconhecido como válido. Tente 'listar ponto_de_parada'.")
    #calcular uma rota pelo ID
    elif cmd == "calcular":
        try:
            val = int(arg)
            found = False
            for rota in rotas:
                if rota.get_id() == val:
                    rota.calc_demanda()
                    found = True
            if not found:
                print(f"A rota com ID:{val} não existe. Tente o comando listar rotas.")
        except ValueError:
            print(f"'{arg}' não é um ID válido para as rotas. Os IDs são do tipo int.")
    #informacao sobre uma pessoa fisica ou juridica
    elif cmd == "informacao":
      found = False
      for list in pessoas:
        for i, pessoa in enumerate(list):
          if  pessoa.getNomeOficial == arg:
            print(f"Nome: {pessoa.getNomeOficial} é do tipo: {pessoa.verificarTipo()}")
            found = True
      if not found:
        print(f"A pessoa fisica ou juridica com o nome '{arg}' não existe. tente listar pessoas.")
    elif cmd == "exibir":
      found = False
      for list in pessoas:
        for i, pessoa in enumerate(list):
          if  pessoa.getNomeOficial == arg:
            print(f"Nome: {pessoa.getNomeOficial} é do tipo: {pessoa.verificarTipo()}")
          pessoa.apresentarDados()
          found = True
      if not found:
         print(f"A pessoa fisica ou juridica com o nome '{arg}' não existe. tente listar pessoas.")
    #relaciona pontos de parada com alunos
    elif cmd == "relacionar_ponto":
        if len(alunos) <= 0:
            print("Não há nenhum aluno registrado no sistema.")
            return
        found = False
        aluno_index = 0
        index = 0

        for aluno in alunos:
            index += 1
            if aluno.getNomeOficial == arg or aluno.getCpfCnpj == arg:
                found = True
                aluno_index = index
        if found:
            print(f"Lista de pontos de parada disponíveis ({len(pontos)}): ")
            index = 0
            for ponto in pontos:
              print(f" - [{index}] nome: {ponto.nome}.")
              index += 1
            ponto_index = SafeInput.get_int(input("Digite o índice do ponto de parada do aluno: "))
            if 0 <= ponto_index < len(pontos):
                alunos[aluno_index - 1].set_ponto_de_parada(pontos[ponto_index])
                print("Ponto de parada relacionado com sucesso.")
            else:
                print(f"O índice '{ponto_index}' é inválido, nenhuma mudança efetuada.")
        else:
            print(f"Não existe nenhum aluno com nome civil ou cpf: '{arg}'.")
    #relaciona um fornecedor com um contrato
    elif cmd == "relacionar_contrato":
      found = False
      fornecedor = None 
      for list in pessoas:
        for pessoa in list:
          if pessoa.getNomeOficial == arg:
              found = True
              fornecedor = pessoa
      #cancela a operacao se não encontrar o fornecedor no sistema
      if not found:
        print(f"A pessoa fisica ou juridica com o nome '{arg}' não existe. tente listar pessoas.")
        return

      print('--Contratos disponíveis: ')
      for i, contrato in enumerate(contratos):
        print(f' [{i}] - contrato: {contrato.num_contrato}.')
      
      index = SafeInput.get_int(input('Digite o index do contrato: '))
      if 0 <= index < len(contratos):
        fornecedor.add_contrato(contratos[index])
        print('Contrato relacionado com sucesso.')
      else:
        print('index invalido')
        
            
          
    else:
        print(f"O comando '{cmd}' não foi reconhecido como um comando válido.")


def test_create_escola():
    handle_command("criar", "escola")

def test_create_aluno():
    handle_command("criar", "aluno")

def test_create_motorista():
    handle_command("criar", "motorista")

def test_create_veiculo():
    handle_command("criar", "veiculo")

def test_create_contrato():
    handle_command("criar", "contrato")

def test_create_fornecedor():
    handle_command("criar", "fornecedor")

def test_create_rota():
    handle_command("criar", "rota")

def test_create_ponto_de_parada():
    handle_command("criar", "ponto_de_parada")

def test_list_rotas():
    handle_command("listar", "rotas")

def test_list_pontos_de_parada():
    handle_command("listar", "pontos_de_parada")

def test_list_pessoas():
    handle_command("listar", "pessoas")

def test_calcular_rota():
    handle_command("calcular", "0")

def test_informacao_pessoa():
    handle_command("informacao", input("nome da pessoa: "))

def test_exibir_pessoa():
    handle_command("exibir", ("nome da pessoa: "))

def test_relacionar_ponto():
  
    handle_command("relacionar_ponto", input("nome do aluno: "))

def test_relacionar_contrato():
    
    handle_command("relacionar_contrato", input("nome do fornecedor: "))

def run_tests(bool):
  if bool:
    print('Rodando Testes:')
    test_create_escola()
    test_create_aluno()
    test_create_motorista()
    test_create_veiculo()
    test_create_contrato()
    test_create_fornecedor()
    test_create_rota()
    test_create_ponto_de_parada()
    test_list_rotas()
    test_list_pontos_de_parada()
    test_list_pessoas()
    test_calcular_rota()
    test_informacao_pessoa()
    test_exibir_pessoa()
    test_relacionar_ponto()
    test_relacionar_contrato()

#roda o app se for o modulo principal
if (__name__ == '__main__'):
  run_tests(test)
  main()
# SchoolBusByVMCinPython

Trabalho Final de UFBA-POO/MATA57-23.2

Este é um projeto em Python para a administração de transporte escolares. Ele permite gerenciar e acompanhar rotas de ônibus escolares, motoristas, contratos, veículos e alunos.

## Conteúdo

- [Overview](#overview)
- [Requerimentos do Sistema](#requerimentos-do-sistema)
- [Executando o Projeto](#como-executar-o-projeto)
- [Funcionalidade](#funcionalidades)
- [Estrutura do Projeto](#estrutura-do-projeto)
- [Uso do Programa](#uso-do-programa)
- [Contribuições](#contribuições)
- [Licença](#licença)

## Overview

Esse sistema foi projetado para gerenciar o transporte de alunos em ônibus escolares. Ele fornece classes para diferentes entidades, como veículos, motoristas, contratos, alunos e muito mais. Os usuários podem interagir com o sistema por meio de uma interface de linha de comando (CLI) para criar, listar e gerenciar essas entidades. Este programa foi primeiramente desenhado para uma matéria na universidade e, portanto, parte da estrutura é modelada apartir do que é solicitado pela matéria.

## Requerimentos do Sistema

- Python 3.10.0
- Git (para contribuição)
- Uma IDE ou editor de código (e.g., Visual Studio Code)(para contribuição)

## Como Executar o Projeto

1. Clone ou baixe repositório para o seu computador.

   ```sh
   git clone https://github.com/vtmattedi/SchoolBusByVMCinPyhton
   ```
2. Certifique-se de ter o Python 3 instalado em sua máquina.
3. Execute o arquivo `main.py` para iniciar o programa interativo.

## Funcionalidades

O projeto SchoolBus By VMC possui as seguintes funcionalidades:

1. Cadastro e gerenciamento de Motoristas.
1. Cadastro e gerenciamento de Fornecedores.
2. Cadastro e gerenciamento de Veículos.
3. Cadastro e gerenciamento de Contratos para motoristas e veículos.
4. Cadastro e gerenciamento de Alunos.
5. Cadastro e gerenciamento de Escolas.
6. Definição de Pontos de Parada para rotas de transporte escolar.
7. Criação e gerenciamento de Rotas de transporte escolar.
8. Cálculo da demanda total de alunos em cada ponto de parada de uma rota.

## Estrutura do Projeto

O projeto SchoolBus by VMC está organizado em classes Java, cada uma representando uma entidade ou funcionalidade do sistema. As principais classes que interagem com o usuário incluem:

- `Motorista`: Representa informações sobre motoristas, incluindo dados pessoais e contratos associados.
- `Veiculo`: Representa informações sobre veículos, incluindo detalhes como placa, modelo e contratos associados.
- `Contrato`: Representa contratos associados a motoristas e veículos.
- `Aluno`: Representa informações sobre alunos, incluindo dados pessoais e associação a escolas e pontos de parada.
- `Escola`: Representa informações sobre escolas, incluindo detalhes de contato e endereço.
- `PontoDeParada`: Representa pontos de parada para rotas de transporte escolar, incluindo a associação de alunos.
- `Rota`: Representa rotas de transporte escolar, incluindo pontos de parada e cálculo de demanda.
- `Pessoa:`: Representa uma pessoa fisica ou juridica. Classes como Escola, Aluno, Motorista e Fornecedor, herdam dela
- `Fornecedor`: Representa informações sobre um fornecedor, incluindo dados da pessoa juridica e uma lista de contratos associados ao fornecedor.

Além diso temos classes de apoio que não interagem diretamente com o usuário:

- ~`debugger`: É uma classe com métodos estáticos responsável pela filtragem do conteúdo exibido utilizado pelo desenvolvedor para testar e construir o sistema e o usuário final.~ Não é utilizado na versão em Python.
- ~`ScannerImpl`: É uma classe apenas com métodos estáticos com a implementação de um scanner único, para que seja possível utilizar ele em diferentes métodos e classes sem ter que fechá-lo (pois da erro fechar e abrir).~ Não é nescessario em Python.
- ~`PersonalInfo`: Representa os dados pessoais de alguém, podendo ser atrelados a um aluno ou motorista.~ (deprecated) não utilizado na versão em Python.
- `Endereço`: Representa um enderenço, contendo todos os dados que necessários para representar um endereço no Brasil.
- Ambos `Endereço` e ~`PersonalInfo`~ foram criados para simplificar o processo de criação dos objetos e reduzir código redundante assim como reduzir a quantidade de variáveis de `Aluno` e `Motorista`.

## Uso do Programa

O SchoolBus By VMC permitirá que você crie e gerencie motoristas, veículos, contratos, alunos, escolas, pontos de parada e rotas. Você também poderá calcular a demanda total de alunos em uma rota específica. Para usar o programa, executar o App.java compilado. No terminal CLI, o menu é intuitivo e autoexplicativo, lá você deverá conseguir fazer tudo que foi descrito em [funcionalidades](#funcionalidades). Atualmente o menu está completamente e unicamente em português além disso, a estrutura das classes foi otimizada para os dados brasileiros.
A única parte mais obscura é relacionar alunos a pontos de parada, para fazer isso, caso haja algum ponto de parada no sistema o aluno pode ser relacionado a algum deles na momento de criação, além disso ele pode ser posteriormente relaciona a um ponto de parada utilizando o comando `relacionar_ponto` seguido de um espaço e o nome civil ou o cpf do aluno, com isso será relatado todos os pontos cadastrados e o usuário pode então escolher qual ponto de parada se deseja relacionar com este aluno. Ela existe pois tecnicamente não foi solicitado, ainda, que a classe aluno seja inicializada com o ponto de parada entretanto a funcionalidade de calcular a demanda de uma rota só faz sentido se houver alunos relacionados a pontos de parada, portanto é feito dessa forma para manter a coerencia entre todas as demandas pedidas pela atividade até o momento em diferentes partes e pode ser que não exista em proximas versões.

## Contribuições

Contribuições são bem-vindas! Sinta-se à vontade para abrir problemas (issues) ou enviar pull requests para melhorar este projeto.
*Guidelines para contribuições*:

- O projeto foi desenvolvido no Brasil, inicialmente para a matéria de Programação Orientada a Objetos pela UFBa, portanto é desejado que métodos públicos tenham variáveis e comentários em português.
- Reciprocidade: quaisquer objetos que estão simultaneamente linkados (exemplo entre `PontosDeParada` e `Aluno`) devem ter de lidar com a reciprocidade, ou seja, se mudar o `PontosDeParada` de `Aluno` deve haver uma mudança tanto no `PontosDeParada` predecessor quanto no sucessor refletindo essa mudança. I.e. eu não devo ter que solicitar que `Aluno` mude seu `PontosDeParada` e o antigo `PontosDeParada` delete `Aluno` e que o novo adicione `Aluno` separadamente.

## Licença

Este projeto é distribuído sob a Licença AGPL-3.0 license. Consulte o arquivo [LICENSE](LICENSE) para obter detalhes.

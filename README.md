# Projeto ouvidoria da Unifacisa - Readme

Este é o repositório da primeira parte do projeto desenvolvido para a competência de linguagem estruturada da universidade Unifacisa.

# Descrição do projeto

O projeto refere-se a um sistema de ouvidoria onde o cliente/usuário poderá realizar manifestações.

# Tecnologias utilizadas

*  Python

# Estrutura do projeto

* services - contém os métodos que realizam as funcionalidades do sistema
* views - contém os métodos de visualização do usuário, agindo como interfaces
* main - contém a aplicação principal

# Funcionalidades do sistema

* Opção 1 - Listagem das manifestações - exibe todas as manifestações cadastradas.
* Opção 2 - Listagem de manifestações por tipo - pede ao usuário que informe o tipo da manifestação e em seguida exibe as manifestações desse tipo.
* Opção 3 - Criar uma nova manifestação - pede ao usuário as informações necessárias para realizar uma manifestação (tipo e descrição) .
* Opção 4 - Exibir quantidade de manifestações - informa a quantidade de manifestações cadastradas.
* Opção 5 - Pesquisar uma manifestação por código - pede ao usuário um código e em seguida exibe a manifestação do correspondente código.
* Opção 6 - Excluir uma manifestação pelo Código - pede ao usuário um código e em seguida o remove.
* Opção 7 - Sair do sistema - encerra a aplicação.

# Tratamento de erros

* Verificação da entrada de dados do usuário, não permitindo que o usuário digite informações incorretas.
* Feedback ao realizar uma operação, sendo ela positiva ou não, exemplo: caso o usuário queira listar as manifestações e não contenha manifestações cadastradas o programa retorará que não existem manifestações cadastradas.

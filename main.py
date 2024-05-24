
from services import *
from utils import *
from views import *


print(sistem_menu())
opcion = read_int("Digite uma opção: ")
while(opcion!=7):
    if(opcion==1):
        print(read_list())
    elif(opcion==2):
        type = read_int("Digite a opção do tipo da manifestação\n 1.Elogio \n 2.Crítica \n 3.Sugestão  \n")
        while(type<1 or type>3):
            type = read_int("Valor inválido,digite um valor válido! \n Digite a opção do tipo da manifestação\n 1.Elogio \n 2.Crítica \n 3.Sugestão  \n")
        print(read_list_type(type))
    elif(opcion==3):
        type = read_int("Digite a opção do tipo da manifestação\n 1.Elogio \n 2.Crítica \n 3.Sugestão  \n")
        while(type<1 or type>3):
            type = read_int("Valor inválido,digite um valor válido! \n Digite a opção do tipo da manifestação\n 1.Elogio \n 2.Crítica \n 3.Sugestão  \n")
        description = input("Digite a manifestação: ")
        print(register_manifestation(type,description))
    elif(opcion==4):
        print(manifestations_quantity())
    elif(opcion==5):
        code = read_int("Digite o código da manifestação: ")
        print(search_manifestation(code))
    elif(opcion==6):
        code = read_int("Digite o código da manifestação que deseja remover: ")
        print(remove_manifestation(code))
    else:
        print("Digite uma opção válida")
    print(sistem_menu())
    opcion = read_int("Digite uma opção: ")
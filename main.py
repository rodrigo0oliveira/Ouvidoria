def sistem_menu():
    print("1) Listagem das Manifestações")
    print("2) Listagem de Manifestações por Tipo")
    print("3)  Criar uma nova Manifestação")
    print("4) Exibir quantidade de manifestações")
    print("5) Pesquisar uma manifestação por código")
    print("6) Excluir uma Manifestação pelo Código")
    print("7) Sair do Sistema.")
    print("")
  
def read_int(msg):
    while True:
        try:
           opcion = int(input(msg))
           return opcion
        except ValueError:
            print("Digite um valor válido!")


def read_list():
    global list_manifestation
    result = ""
    if(len(list_manifestation)>0):
        for manifestations in list_manifestation:
            result += f"Código: {manifestations['code']}, Manifestação: {manifestations['manifestation']}\n"
        return result
    else:
        return "Não existem manifestações cadastradas!"
        
def read_list_type(type):
    global list_manifestation
    result = ""
    if(len(list_manifestation)>0):
        for manifestation in list_manifestation: 
            if(manifestation['type']==type):
                result += f"Código: {manifestation['code']},Tipo: {manifestation['type']}, Manifestação: {manifestation['manifestation']}\n"
        return result   
    else:
        return "Não existem manifestações cadastradas!"
        
def register_manifestation(code,type,manifestation):
    global counter_list
    new_manifestation = {
        "code": code,
        "type": type,
        "manifestation": manifestation
    }
    list_manifestation.append(new_manifestation)
    counter_list += 1
    return "Manifestação cadastrada!"
    
    
def manifestations_quantity():
    if(counter_list>0):
        return  "A ouvidoria possui "+counter_list+" manifestações"
    else:
        return "A ouvidoria não possui manifestações cadastradas!"


def search_manifestation(code):
    global list_manifestation
    if(len(list_manifestation)>0):
        for manifestation in list_manifestation:
            if(manifestation['code'] == code):
               return f"Código: {manifestation['code']},Tipo: {type['type']}, Manifestação: {manifestation['manifestation']}"
    else:
        return "Não existem manifestações cadastradas!"


def remove_manifestation(code):
    global counter_list
    if(len(list_manifestation)>0):
         for index,manifestation in enumerate(list_manifestation):
             if(manifestation['code'] == code):
                 del list_manifestation[index]
                 counter_list -= 1
                 return "Manifestação removida!"
         return "Código não encontrado"    
    else:
        return "Não existem manifestações cadastradas!"


if __name__ == 'main'=
    print(sistem_menu())
    opcion = read_int("Digite uma opção: ")
    while(opcion!=7):
        if(opcion==1):
            print(read_list(list_manifestation))
        elif(opcion==2):
            type = input("Digite o tipo da manifestação: ")
            print(read_list_type(type))
        elif(opcion==3):
            code = read_int("Digite o código da manifestação: ")
            type = input("Digite o tipo da manifestação: ")
            description = input("Digite a manifestação: ")
            print(register_manifestation(code,type,description))
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
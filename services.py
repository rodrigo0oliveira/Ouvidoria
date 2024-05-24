from utils import *

list_manifestation = []
counter_list = 0
autoincrement_code = 1


def read_list():
    global list_manifestation
    result = ""
    if(len(list_manifestation)>0):
        for manifestation in list_manifestation:
            result += f"Código: {manifestation['code']},Tipo: {manifestation['type']}, Manifestação: {manifestation['manifestation']}\n"
        return result
    else:
        return "Não existem manifestações cadastradas!"
        
def read_list_type(type):
    global list_manifestation
    tipo = ""
    if(type==1):
        tipo = "Elogio"
    elif(type==2):
        tipo = "Crítica"
    elif(type==3):
        tipo = "Sugestão"

    list_type = ""
    if(len(list_manifestation)>0):
        for manifestation in list_manifestation: 
            if(manifestation['type']==tipo):
                list_type += f"Código: {manifestation['code']},Tipo: {manifestation['type']}, Manifestação: {manifestation['manifestation']} \n"
        return list_type   
    else:
        return "Não existem manifestações cadastradas!"
        
def register_manifestation(type,manifestation):
    global counter_list
    global autoincrement_code

    if(type==1):
        tipo = "Elogio"
    elif(type==2):
        tipo = "Crítica"
    elif(type==3):
        tipo = "Sugestão"
        
    new_manifestation = {
        "code": autoincrement_code,
        "type": tipo,
        "manifestation": manifestation
    }
    list_manifestation.append(new_manifestation)
    counter_list += 1
    autoincrement_code += 1
    return "Manifestação cadastrada! \n"
    
    
def manifestations_quantity():
    if(counter_list==1):
        return  "A ouvidoria possui ",counter_list," manifestação cadastrada"
    elif(counter_list>1):
        return "A ouvidoria possui",counter_list,"manifestações cadastradas!"
    else:
        return "A ouvidoria não possui manifestações cadastradas!"


def search_manifestation(code):
    global list_manifestation
    string = ""
    if(len(list_manifestation)>0):
        for manifestation in list_manifestation:
            if(manifestation['code'] == code):
               string += f"Código: {manifestation['code']},Tipo: {manifestation['type']}, Manifestação: {manifestation['manifestation']} "
            
            
    else:
        string = "Não existem manifestações cadastradas! \n"
        
    return string


def remove_manifestation(code):
    global counter_list
    if(len(list_manifestation)>0):
         for index,manifestation in enumerate(list_manifestation):
             if(manifestation['code'] == code):
                 del list_manifestation[index]
                 counter_list -= 1
                 return "Manifestação removida! \n"
               
    else:
        return "Não existem manifestações cadastradas! \n "

def read_int(msg):
    while True:
        try:
           opcion = int(input(msg))
           return opcion
        except ValueError:
            print("Digite um valor válido!")
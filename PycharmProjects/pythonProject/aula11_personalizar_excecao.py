class Error(Exception):
    pass

class InputError(Error):
    def __init__(self, message):
        self.message = message

while True: #laço de repetição eterno, enquanto der erro no try/exception ele volta ao inicio
    try:
        x = int(input('Entre com uma nota de 0 a 10: '))
        print(x)
        if x > 10:
            raise InputError('Nota não pode ser maior que 10') #raise força uma excessão
        elif x < 0:
            raise InputError('Nota não pode ser menor que 0')
        break
    except ValueError:
        print('Valor inválido. Deve-se digitar apenas números')
    except InputError as ex:
        print(ex)
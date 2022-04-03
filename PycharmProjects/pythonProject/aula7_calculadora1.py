#função é tudo que retorna um valor, método é que não retorna

# #declarando um método
# def soma(a, b):
#     return a + b
#
# def subtracao(a, b):
#     return a - b
#
# def multiplicacao(a, b):
#     return a * b
#
# def divisao(a, b):
#     return a / b
#
# print(soma(1, 2))
# print(subtracao(5, 9))
# print(multiplicacao(4, 9))
# print(divisao(33, 3))


#criando uma classe
class Calculadora:
    def __init__(self, num1, num2):
        self.a = num1
        self.b = num2
    def soma(self):
        return self.a + self.b

    def subtracao(self):
        return self.a - self.b

    def multiplicacao(self):
        return self.a * self.b

    def divisao(self):
        return self.a / self.b

# #instanciando uma classe
# calculadora = Calculadora(9, 12)
# print(calculadora.soma())
# print(calculadora.subtracao())
# print(calculadora.multiplicacao())
# print(calculadora.divisao())

if __name__ == '__main__':
    calculadora = Calculadora(9, 12)
    print(calculadora.soma())
    print(calculadora.subtracao())
    print(calculadora.multiplicacao())
    print(calculadora.divisao())
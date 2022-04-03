contador_letras = lambda lista: [len(x) for x in lista]
#com o lambda pode ser resolvido com funções simples, de uma linha
#funções mais complexas não vão funcionar no lambda

lista_animais = ['cachorro', 'gato', 'bizão', 'elefante']
print(contador_letras(lista_animais))

#calculadora com lambda
soma = lambda a, b: a + b
subtracao = lambda a, b: a - b
print(soma(5, 10))
print(subtracao(10, 5))

#fazendo um discionario com lambda
calculadora = {
    'soma': lambda a, b: a + b,
    'subtracao': lambda a, b: a - b,
    'multiplicacao': lambda a, b: a * b,
    'divisao': lambda a, b: a / b,
}

print(type(calculadora))
soma = calculadora['soma']
multiplicacao = calculadora['multiplicacao']
print('A soma é: {}'.format(soma(10, 5)))
print('A multiplicação é: {}'.format(multiplicacao(10, 2)))
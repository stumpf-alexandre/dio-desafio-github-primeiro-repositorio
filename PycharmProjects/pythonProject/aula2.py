#a = 10
#b = 5
a = int(input('Entre com o primeiro valor: '))
b = int(input('Entre com o segundo valor: '))
soma = a + b
subtracao = a - b
multiplicacao = a * b
divisao = a / b
resto = a % b
print(type(soma))#o type mostra qual é a variavel
print(soma)
print(subtracao)
print(multiplicacao)
print(divisao)
print(type(divisao))#o type mostra qual é a variavel
print(int(divisao))#transformando float para int
print(resto)

print('soma: ' + str(soma))#concatenando int com string
#ou
print('soma: {}'.format(soma))

print('Soma: {}. Subtração: {}'.format(soma, subtracao))
#ou
resultado = ('Soma: {soma} '\
            '\nSubtração: {subt} '\
            '\nMultiplicação: {mult} '\
            '\nDivisão: {div} '
            '\nResto: {rest}'.format(soma = soma, subt = subtracao, mult = multiplicacao, div = divisao, rest = resto))

print(resultado)

x = '1'
soma2 = int(x) + 1#string para int
print(soma2)
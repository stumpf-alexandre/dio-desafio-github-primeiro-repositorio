import random
import string

tamanho = int(input("Digite a quantidade de caracteres da sua senha: "))

chars = string.ascii_letters + string.digits + 'Çç!@#$%&*()-=+,.;:/?' #gera na senha letras maiusculas e minusculas
rnd = random.SystemRandom()
print(''.join(rnd.choice(chars)for i in range(tamanho)))
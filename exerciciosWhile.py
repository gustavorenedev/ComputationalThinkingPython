# 1) imprima a tabuada do número 5, de 0 e 10, inclusive. Depois, adapte o programa para receber dois números do
# usuário: o de início e o de fim faça este exercício uma vez utilizando o for, e outra utilizando o while

# Tabuada com for:
# num = int(input("Digite o número que você gostaria de ver a tabuada: "))
# num_max = int(input("Digite até quanto você quer a tabuada: "))

# for i in range(1, num_max + num):
#    print(f"{num}x{i - 1} = {num * i - num}")
# print("Fim")

# Tabuada com while:

# num = int(input("Digite o número que você gostaria de ver a tabuada: "))
# c = 0

# while c < 10 + 1:
#    print(f"{num}x{c} = {num * c}")
#    c += 1


# 2) faça um programa que imprima a soma dos números inteiros positivos de 1 a 100 com for.
# soma = 0
# for i in range(1, 101):
#    soma = soma + i
# print(soma)

# 2) faça um programa que imprima a soma dos números inteiros positivos de 1 a 100 com while.

# c = 0
# soma = 0
# while c < 101:
#     soma += c
#     c += 1
# print(soma)

# 3) Solicitar um número obrigatoriamente inteiro positivo do usuário, e calcular seu fatorial
# fatorial de um número é a multiplicação dele com todos os que vieram antes dele (sem o 0)
# ex: 3! = 3*2*1 = 6
# ex: 0! = 1


# fatorial com while
# num = int(input("Digite o valor inteiro e positivo no qual deseja o fatorial: "))
# c = num
# para começarmos com uma multiplicação limpa iniciamos o programa multiplicando por 1
# f = 1

# print(f"Fatorial de {num}! = ", end=' ')
# enquanto contador for maior que 0
# while c > 0 and num >= 0:

#     print(f"{c}", end=' ')
    # se o c for maior que 1 mostre um 'x' senão mostre um '='
#     print(" x " if c > 1 else ' = ', end=' ')
#     f *= c
#     c -= 1
# print(f"{f}.")


# 4) Solicite dois número ao usuário, sendo que o segundo deverá ser obrigatoriamente
# maior que o primeiro
# print("O 2º número deverá ser obrigatoriamente maior que o 1º")

# num1 = float(input("Digite o 1º número: "))
# num2 = float(input("Digite o 2º número: "))

# while num1 >= num2:
#    if num1 == num2:
#        print(f"O 1ª({num1}) número é igual ao 2º({num2}) número")
#        num2 = float(input("Digite o 2º número novamente: "))
#    elif num1 > num2:
#        print(f"O 1ª({num1}) número continua sendo maior que o 2º({num2}) número")
#        num2 = float(input("Digite o 2º número novamente: "))


# 5) solicite 2 números ao usuário. Para cada número do 1 ao primeiro número, faça a tabuada dele do 0 até o
# segundo número
# print("Digite dois números, o 1º número fará a tabuada dele e o 2º número mostrará até onde irá")

# num = int(input("Digite o número que você gostaria de ver a tabuada: "))
# num_max = int(input("Digite até quanto você quer a tabuada: "))
# c = 0

# while c < num_max + 1:
#    print(f"{num}x{c} = {num * c}")
#    c += 1
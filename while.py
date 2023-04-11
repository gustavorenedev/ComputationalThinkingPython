## While (enquanto)
# damos a condição que tem que ser verdade para o loop continuar
# condição tem que ser dada antes dele

numero = 0

while numero <= 5: # é apenas uma comparação. Eu não altero o valor do número
    print(numero)
    # tenho que ter um incremento manual do meu contador
    numero += 1

# fora do loop
print("fora do loop")
print(numero)

# forçar a ser ímpar
# eu tenho que agir enquanto não for impar

n = int(input("Diga um número ímpar positivo para a quantidade de linhas para a figura: "))

# enquanto o número for par o loop continua
# agora quando numero for impar acaba
while n % 2 == 0:
    # o loop só vai para quando condição for satisfeita
    print("Este número é par. Por favor digite um número ímpar")
    n = int(input("Diga um número ímpar positivo para a quantidade de linhas para a figura: "))

# loop enquanto o usuário quiser:
resposta = "sim"

while resposta == "sim":
    resposta = input("Deseja continuar ? 'sim' ou 'não'").lower()

while resposta != "não":
    resposta = input("Deseja continuar ? 'sim' ou 'não'").lower()

# forçar a ser ímpar e positivo

# enquanto a resposta for errada, pedir para alterar
while (n % 2 == 0) or (n < 0):
    print("Você não digitou um número nas condições que eu pedi")
    n = int(input("Diga um número ímpar positivo para a quantidade de linhas"))

## Exercícios

# 1) imprima a tabuada do número 5, de 0 e 10, inclusive.
# Depois, adapte o programa para receber dois números do usuário: o de início e o de fim
# faça este exercício uma vez utilizando o for, e outra utilizando o while

# 2) faça um programa que imprima a soma dos números inteiros positivos de 1 a 100, inclusive
# faça este exercício uma vez utilizando o for, e outra utilizando o while

# 3) Solicitar um número obrigatoriamente inteiro positivo
# do usuário,
# e calcular seu fatorial
##fatorial de um número é a multiplicação dele com todos os que vieram antes dele (sem o 0)
## ex: 3! = 3*2*1 = 6
## ex: 0! = 1


# 4) Solicite dois número ao usuário,
# sendo que o segundo deverá ser obrigatoriamente
# maior que o primeiro

# 5) solicite 2 números ao usuário. Para cada número do 1 ao primeiro número, faça a tabuada dele do 0 até o segundo número

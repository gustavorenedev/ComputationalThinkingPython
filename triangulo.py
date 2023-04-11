# 1) agora, refaça o exercício acima, sendo que o número de linhas vai ser um número escolhido pelo usuário
fim = int(input("Digite em números inteiros quantas linhas você quer q a piramide tenha: "))

for i in range (1,fim + 1):
    if i <= (fim + 1) / 2:
        print("*" * i)
    else:
        print("*" * (fim + 1 - i))

# 2) imprima a tabuada do número 5, de 0 e 10, inclusive. Depois, adapte o programa para receber dois números
# do usuário: o de início e o de fim
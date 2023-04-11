# 3) faça um programa que imprima a soma dos números inteiros positivos de 1 a 100, inclusive
soma = 0
for i in range(1, 101):
    soma = soma + i
print(soma)

# fatorial

numero = int(input("Digite um número: "))
fatorial = 1

for i in range(1, numero+1):
    fatorial = fatorial * i

print("O fatorial de", numero, "é", fatorial)





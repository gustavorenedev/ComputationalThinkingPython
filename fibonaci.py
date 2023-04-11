# 2) imprima apenas o quinto elemento da sequencia
# fibonacci (onde um novo elemento é a soma dos 2 anteriores,
# e por definição tem como primeiro o 0, e segundo o 1)

# fibonacci é a soma dos 2 números anteriores: 0,1,1,2,3,5,8,13,21
soma = 0
n1 = 0
n2 = 1

for i in range(3, 6):
    soma = n1 + n2
    n1 = n2
    n2 = soma

print(soma)


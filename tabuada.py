#num = int(input("Digite o número para gerar a tabuada: "))
#num_max = int(input("Digite até qual número você quer que a tabuada vá: "))
#cont = 0
#fim = num * num_max + num
#soma = 0

# for i in range(0, fim, num):

#    print(f"{num} x {cont} = {soma}")
#    cont = cont + 1
#    soma = soma + num

# Tabuada refatorada
num = int(input("Digite o número que você gostaria de ver a tabuada: "))
num_max = int(input("Digite até quanto você quer a tabuada: "))

for i in range(1, num_max + num):
    print(f"{num}x{i - 1} = {num * i - num}")
print("Fim")



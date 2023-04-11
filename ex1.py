
## EXERCÍCIOS
# 1)para cada numero de 0 a 4, imprima a soma dos anteriores
# a ele (positivos)

'''
vamos escrever os números anteriores (positivos) a cada um e sua soma
0: nenhum -> 0
1: 0      -> 0
2: 1,0    -> 1
3: 2,1,0  -> 3
4: 3,2,1,0-> 6
'''
# soma=0
# # lembrando que range(5) = [0,1,2,3,4]
# for i in range(5): #para cada numero de 0 a 4
#     print(i)
#     soma+=i  #igual a soma=soma+i , ou seja, eu pego o que eu tinha e adiciono um número

# vemos aqui que a soma dos ultimos 2 numero do lado esquerdo, forma do lado direito a resposta
soma = 0
for i in range(5):
    soma += i
    print(i, soma)

# 3)Faça um programa em loop que imprima esta imagem:
'''
*
**
***
****
*****
****
***
**
*
'''

for i in range (1,10):
    if i <= 5:
        print("*" * i)
    else:
        print("*" * (10-i))

## EXERCÍCIOS
# 1) agora, refaça o exercício acima, sendo que o número de linhas vai ser um número escolhido pelo usuário
fim = int(input("Digite em números inteiros quantas linhas você quer q a piramide tenha: "))

for i in range (1,fim):
    if i <= (fim / 2):
        print("*" * i)
    else:
        print("*" * (fim-i))





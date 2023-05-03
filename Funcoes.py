## FUNÇÕES/PROCEDIMENTOS

'''
sintaxe função
def nome(arg):
    [...]
    return variavel
naõ precisa return se serve pra alterar
return = retorna algo
(arg) = valores que você vai passar para as linhas de código dentro
nome = nome da função
def = definição
'''

def solicita_numero(condicao):
    numero = float(input(f"Digite um número {condicao}:"))
    return numero

def verificaNumeroPar(numero):
    while numero % 2 != 0:
        print("Você não digitou um número par")
        numero = solicita_numero("par")
    return numero

def solicitaNumeroPar():
    numeroPar = solicita_numero("par")
    numeroPar = verificaNumeroPar(numeroPar)
    return numeroPar

numero = solicita_numero()

## criando a função
                ## pode escrever qualquer coisa
# def print_formatado(numero):
#     print(f"{numero:.2f}")
#
# ## executar(chamar) a função
# print_formatado(numero) #aqui tem que ser uma variável já existente





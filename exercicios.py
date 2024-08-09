# 1. Precisamos imprimir um número para cada andar de um hotel de 20 andares. Porém, o dono do hotel é supersticioso e optou por não ter um 13ro andar.Escreva um código que imprima todos os números exceto o número 13. Escreva mais um código que resolva o mesmo problema, mas dessa vez usando o laço de repetição 'while'.Como desafio, imprima eles em ordem decrescente (20, 19, 18...)

# andar = 20

# while andar > 0:
#     if andar != 13:
#         print(andar)
#     andar -= 1
    

# 2. Faça uma função calculadora de dois números com três parâmetros: os dois primeiros serão os números da operação e o terceiro será a entrada que definirá a operação a ser executada. Considera a seguinte definição:
# 1. Soma
# 2. Subtração
# 3. Multiplicação
# 4. Divisão

# Caso seja inserido um número de operação que não exista, o resultado deverá ser 0.

# def calculadora (num1, num2, operacao):
#     if operacao == 1:
#         return num1 + num2
#     elif operacao == 2:
#         return num1 - num2
#     elif operacao == 3:
#         return num1 * num2
#     elif operacao == 4:
#         if num2 != 0:
#             return num1 / num2
#         else:
#             return "Erro: Divisão por zero"
#     else:
#         return 0

# print(calculadora(2,6,4))

# 3. Desenvolva um programa que recebe do usuário nome completo e ano de nascimento que seja entre 1922 e 2021.
# A partir dessas informações, o sistema mostrará o nome do usuário e a idade que completou, ou completará, no ano atual (2022).

# Caso o usuário não digite um número ou apareça um inválido no campo do ano, o sistema informará o erro e continuará perguntando até que um valor correto seja preenchido.

nome_completo = input("digite seu nome: ")

while True:
    try:
        ano_nascimento = int(input("digite seu ano de nascimento entre 1922 e 2021: "))
        if ano_nascimento > 1922 and ano_nascimento < 2021:
            idade = 2022 - ano_nascimento
            print(f" {nome_completo} você têm {idade} anos")
            break
        else:
            print("ano invalido")
    except ValueError:
        print("digite seu ano de nascimento entre 1922 e 2021")
    
# Faça uma função calculadora que os números e as operações serão feitas pelo usuário. O código deve ficar rodando infinitamente até que o usuário escolha a opção de sair. No início, o programa mostrará a seguinte lista de operações:

# 1: Soma
# 2: Subtração
# 3: Multiplicação
# 4: Divisão
# 0: Sair

# Digite o número para a operação correspondente e caso o usuário introduza qualquer outro, o sistema deve mostrar a mensagem “Essa opção não existe” e voltar ao menu de opções.

# Após a seleção, o sistema deve pedir para o usuário inserir o primeiro e segundo valor, um de cada. Depois precisa executar a operação e mostrar o resultado na tela. Quando o usuário escolher a opção “Sair”, o sistema irá parar.

# É necessário que o sistema mostre as opções sempre que finalizar uma operação e mostrar o resultado. 

def soma(num1,num2):
    return num1 + num2

def subtracao(num1,num2):
    return num1 - num2

def multiplicacao(num1,num2):
    return num1 * num2

def divisao(num1,num2):
    return num1 / num2

def menu_operacao():
    while True:
        print("\nEscolha uma opção de operação:")
        print("1. Soma")
        print("2. Subtração")
        print("3. Multiplicação")
        print("4. Divisão")
        print("0. Sair")
        opcao = input("Digite o número da opção desejada (1, 2, 3, 4 ou 0): ")

        if opcao == "1":
            num1 = float(input("Digite o primeiro número: "))
            num2 = float(input("Digite o segundo número: "))
            resultado = soma(num1, num2)
            print(f"Resultado da Soma: {resultado}")
        elif opcao == "2":
            num1 = float(input("Digite o primeiro número: "))
            num2 = float(input("Digite o segundo número: "))
            resultado = subtracao(num1, num2)
            print(f"Resultado da Subtração: {resultado}")
        elif opcao == "3":
            num1 = float(input("Digite o primeiro número: "))
            num2 = float(input("Digite o segundo número: "))
            resultado = multiplicacao(num1, num2)
            print(f"Resultado da Multiplicação: {resultado}")
        elif opcao == "4":
            num1 = float(input("Digite o primeiro número: "))
            num2 = float(input("Digite o segundo número: "))
            resultado = divisao(num1, num2)
            print(f"Resultado da Divisão: {resultado}")
        elif opcao == "0":
            print("Tchau")
            break
        else:
            print("Opção inválida. Por favor, escolha 1, 2, 3, 4 ou 0.")

menu_operacao()
import pyfiglet

texto = pyfiglet.figlet_format("Calculadora")

print(texto)


import math

def soma(a, b):
    return a + b

def subtracao(a, b):
    return a - b

def multiplicacao(a, b):
    return a * b

def divisao(a, b):
    if b != 0:
        return a / b
    else:
        return "Erro! Divisão por zero."

def potencia(a, b):
    return a ** b

def raiz_quadrada(a):
    if a >= 0:
        return math.sqrt(a)
    else:
        return "Erro! Raiz quadrada de número negativo."

def menu():
    print("Escolha uma operação:")
    print("1. Soma")
    print("2. Subtração")
    print("3. Multiplicação")
    print("4. Divisão")
    print("5. Potência")
    print("6. Raiz Quadrada")
    print("7. Sair")

def calculadora():
    while True:
        menu()
        escolha = input("Digite o número da operação desejada: ")
        print("-"*45)

        if escolha == '7':
            print("Saindo da calculadora...")
            break

        if escolha in ['1', '2', '3', '4', '5']:
            num1 = float(input("Digite o primeiro número: "))
            num2 = float(input("Digite o segundo número: "))

        if escolha == '1':
            print(f"O resultado da soma é: {soma(num1, num2)}")
        elif escolha == '2':
            print(f"O resultado da subtração é: {subtracao(num1, num2)}")
        elif escolha == '3':
            print(f"O resultado da multiplicação é: {multiplicacao(num1, num2)}")
        elif escolha == '4':
            print(f"O resultado da divisão é: {divisao(num1, num2)}")
        elif escolha == '5':
            print(f"O resultado da potência é: {potencia(num1, num2)}")

        elif escolha == '6':
            num = float(input("Digite o número para calcular a raiz quadrada: "))
            print(f"O resultado da raiz quadrada é: {raiz_quadrada(num)}")
        else:
            print("Opção inválida!")

if __name__ == "__main__":
    calculadora()

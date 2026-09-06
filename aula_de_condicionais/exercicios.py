#Escreva um programa que leia um número inteiro e informe se ele é par ou ímpar. 
# Utilize try-except para garantir que o programa não quebre caso o usuário digite texto em vez de números;

numero = input("Digite um número inteiro: ")

try:
    numero = int(numero)
    if numero % 2 == 0:
        print(f"O número {numero} é par.")
    else:
        print(f"O número {numero} é ímpar.")
except ValueError:
    print("Por favor, digite um número inteiro válido.")

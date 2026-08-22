print("Números primos:")
number = int(input('Digite um número: '))

def is_prime():
    if number %2 == 0:
        print(f'O número {number} não é primo.')
    else:
        print(f'O número {number} é primo.')

is_prime()
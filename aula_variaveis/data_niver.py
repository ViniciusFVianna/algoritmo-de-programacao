atualYear = 2026

print("Digite o ano do seu nascimento: ")
birthDate = int(input())

def calculateAge(birthDate, atualYear):
    return atualYear - birthDate

age = calculateAge(birthDate, atualYear)
print(f"Você tem {age} anos.")
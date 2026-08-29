print("Calculadora Salarial!!!")
print("==========================")

valor_hora = 14.25
horas_normais = 163
horas_extras = 20

def calcular_salario(valor_hora, horas_normais, horas_extras):
    salario_normal = valor_hora * horas_normais
    salario_extra = valor_hora * 2
    salario_total = salario_normal + salario_extra
    return salario_total

salario_final = calcular_salario(valor_hora, horas_normais, horas_extras)
print(f"Salário final: R$ {salario_final:.2f}")

print("==========================")
print("Fim do programa.")
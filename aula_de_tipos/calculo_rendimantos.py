print("Vamos fazer o cáculo do seu rendimento mensal!!!")
print("===================================================")

salario_fixo = float(input("Digite o valor do salário fixo: "))
comissao = float(input("Digite o valor da comissão (em decimal): "))
vendas_mes = float(input("Digite o valor total das vendas do mês: "))

total_ganho = salario_fixo + (vendas_mes * comissao)

output = f"""
Salário fixo: R$ {salario_fixo:.2f}
Comissão: R$ {vendas_mes * comissao:.2f}
Total ganho no mês: R$ {total_ganho:.2f}
"""

print(output)
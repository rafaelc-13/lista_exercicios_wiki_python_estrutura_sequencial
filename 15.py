'''
15)Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês.
Calcule e mostre o total do seu salário no referido mês, sabendo-se que são descontados 11% para o Imposto de Renda,
8% para o INSS e 5% para o sindicato, faça um programa que nos dê:
a)salário bruto.
b)quanto pagou ao INSS.
c)quanto pagou ao sindicato.
d) o salário líquido.
calcule os descontos e o salário líquido, conforme a tabela abaixo:
+ Salário Bruto : R$
- IR (11%) : R$
- INSS (8%) : R$
- Sindicato ( 5%) : R$
= Salário Liquido : R$
Obs.: Salário Bruto - Descontos = Salário Líquido.
'''

ganho_hora = float(input("Quanto você ganha por hora? "))
horas_trabalhadas = int(input("Quantas horas voce trabalha por mês? "))
bruto = ganho_hora * horas_trabalhadas

imposto = (0.11 * bruto)
INSS = (0.08 * bruto)
sindicato = (0.05 * bruto)
descontos = imposto + INSS + sindicato
sal_liquido = bruto - descontos

print(f'''
+ Salário Bruto : R$ {bruto}
- IR (11%) : R$ {imposto}
- INSS (8%) : R$ {INSS}
- Sindicato ( 5%) : R$ {sindicato}
= Salário Liquido : R$ {sal_liquido}
''')





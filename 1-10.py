'''1)Faça um Programa que mostre a mensagem "Alo mundo" na tela.'''
print("Alo mundo")
print("-="*11)

'''2)Faça um Programa que peça um número e então mostre a mensagem 
O número informado foi [número]'''
n = int(input("Numero: "))
print("O número informado foi",n)
print("-="*11)

'''3)Faça um Programa que peça dois números e imprima a soma.'''
n1 = int(input("1º valor: "))
n2 = int(input("2º valor: "))
soma = n1 + n2
print("A soma foi", soma)
print("-="*11)

'''4)Faça um Programa que peça as 4 notas bimestrais e mostre a média.'''
n1 = int(input("Primeira nota: "))
n2 = int(input("Segunda nota: "))
n3 = int(input("Terceira nota: "))
n4 = int(input("Quarta nota: "))
soma = n1 + n2 + n3 + n4
media = soma/4
print("A media foi", media)
print("-="*11)

'''5)Faça um Programa que converta metros para centímetros.'''
metros = float(input("Quantos metros? "))
centimetros = metros * 100
print("Isso equivale a",centimetros,"centimetros.")
print("-="*11)

'''6)Faça um Programa que peça o raio de um círculo, calcule e mostre sua área.'''
r = float(input("Qual o raio do circulo? (m) "))
pi = 3.14
area = pi * ( r ** 2 )
print("A área desse circulo é de ",area," metros.")
print("-="*11)

'''7)Faça um Programa que calcule a área de um quadrado, em seguida 
mostre o dobro desta área para o usuário.'''
lado = float(input("Quanto vale um dos lados do quadrado? "))
area = lado ** 2
print(f"Considerando sua área, {area}. O dobro dela vale {area*2}.")
print("-="*11)

'''8)Faça um Programa que pergunte quanto você ganha por hora
 e o número de horas trabalhadas no mês. Calcule e mostre o total do seu salário no referido mês.'''
sal_hor = float(input("Quanto você ganha por hora? "))
hor_trab = int(input("Quantas horas você trabalha por mês? "))
sal_tot = sal_hor * hor_trab
print("Seu salário será de: R$",sal_tot)
print("-="*11)

'''9)Faça um Programa que peça a temperatura em graus Fahrenheit,
 transforme e mostre a temperatura em graus Celsius. C = 5 * ((F-32) / 9).'''
F = float(input("Qual a temperatura local em Fº? "))
C = 5 * ((F-32) / 9)
print(f"Isso equivale a {C}Cº")
print("-="*11)

'''10)Faça um Programa que peça a temperatura em graus Celsius,
 transforme e mostre em graus Fahrenheit.'''
c = float(input("Qual a temperatura local em Cº? "))
fahr = (c * 1.8) + 32
print(f"Isso equivale a {fahr}Fº")
print("-="*11)



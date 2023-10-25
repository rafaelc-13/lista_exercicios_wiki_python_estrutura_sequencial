'''
16)Faça um programa para uma loja de tintas. O programa deverá pedir o tamanho em metros quadrados da área a ser pintada.
 Considere que a cobertura da tinta é de 1 litro para cada 3 metros quadrados e que a tinta é vendida em latas de 18 litros,
  que custam R$ 80,00. Informe ao usuário a quantidades de latas de tinta a serem compradas e o preço total.
'''

tamanho = float(input("Qual o tamanho em m², da área a ser pintada?  "))
cobertura = tamanho / 3
latas = 1

while cobertura > 18:
    latas += 1
    cobertura -= 18

preco_lata = 80
preco_tot = latas * preco_lata
print (f'Foram utilizadas {latas} latas.')
print(f'Essas latas custarão {preco_tot}R$')

# 1l/3m²
# 18l

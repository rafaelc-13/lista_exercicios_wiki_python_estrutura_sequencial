'''
17)Faça um Programa para uma loja de tintas. O programa deverá pedir o tamanho em metros quadrados da área a ser pintada.
Considere que a cobertura da tinta é de 1 litro para cada 6 metros quadrados e que a tinta é vendida em latas de 18 litros, que custam R$ 80,00 ou em galões de 3,6 litros, que custam R$ 25,00.
Informe ao usuário as quantidades de tinta a serem compradas e os respectivos preços em 3 situações:
comprar apenas latas de 18 litros;
comprar apenas galões de 3,6 litros;
misturar latas e galões, de forma que o desperdício de tinta seja menor. Acrescente 10% de folga e sempre arredonde os valores para cima, isto é, considere latas cheias.
'''

area_a_pintar = float(input("Áreas em m² a ser pintada: "))
cobertura = area_a_pintar / 6
folga = cobertura * 0.1
cobertura += folga


def opt1 (cobertura):
    latas = (cobertura / 18)
    gasto = int(latas) * 80
    return f'A R$80, comprando {latas} latas, você gastaria: R$ {gasto:.2f}'

def opt2 (cobertura):
    galoes = (cobertura / 3.6)
    gasto = int(galoes) * 25
    return f'A R$25, comprando {galoes} galoes, você gastaria: R$ {gasto:.2f}'

def opt3 (cobertura):
    latas = int(cobertura/18)
    cobertura -= latas * 18
    galoes = (cobertura / 3.6)
    gasto = int(latas) * 80 + int(galoes) * 25
    return f'Comprando {int(latas)} latas a 80R$ e {int(galoes)} galoes a 25R$, você gastaria: R$ {gasto:.2f}'

escolha = int(input('''
1-comprar apenas latas de 18 litros;
2-comprar apenas galões de 3,6 litros;
3-misturar latas e galões:
'''))

if escolha == 1:
    print (opt1(cobertura))
elif escolha == 2:
    print (opt2(cobertura))
elif escolha == 3:
    print (opt3(cobertura))




'''
11)Faça um Programa que peça 2 números inteiros e um número real.
Calcule e mostre:
o produto do dobro do primeiro com metade do segundo .
a soma do triplo do primeiro com o terceiro.
o terceiro elevado ao cubo.
'''
n1 = int(input("Digite 1º valor:"))
n2 = int(input("Digite 2º valor:"))
n3 = float(input("Digite 3º valor:"))

conta_1 = (n1*2) * (n2/2)
conta_2 = (n1*3) + n3
conta_3 = n3 ** 3

print(f"O produto do dobro do primeiro com metade do segundo é {conta_1}. \n"
      f"A soma do triplo do primeiro com o terceiro é {conta_2}. \n"
      f"O terceiro elevado ao cubo é {conta_3}.")

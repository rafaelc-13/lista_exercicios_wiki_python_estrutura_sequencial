'''
13)Tendo como dado de entrada a altura (h) de uma pessoa, construa um algoritmo que calcule seu peso ideal, utilizando as seguintes fórmulas:
Para homens: (72.7*h) - 58
Para mulheres: (62.1*h) - 44.7
'''
h =  float(input("Sua altura em metros: "))
while True:
    sexo = input("Seu sexo é M-masculino ou F-feminino? ").upper()
    if sexo == 'M':
        sexo == 'Masculino'
        peso_ideal = (72.7 * h) - 58
        print(f'Devido o fato de você ser do sexo {sexo}, seu peso ideal é {peso_ideal}')
        break
    elif sexo == 'F':
        sexo == 'Feminino'
        peso_ideal = (62.1 * h) - 44.7
        print(f'Devido o fato de você ser do sexo {sexo}, seu peso ideal é {peso_ideal}')
        break
    else:
        print("Sexo inválido, não da para determinar peso ideal.")


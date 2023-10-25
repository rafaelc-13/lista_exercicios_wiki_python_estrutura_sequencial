'''
18)Faça um programa que peça o tamanho de um arquivo para download (em MB) e a velocidade de um link de Internet (em Mbps),
 calcule e informe o tempo aproximado de download do arquivo usando este link (em minutos).
'''
tamanho = float(input("Qual o tamanho do arquivo(em Mb)? "))
vel = float(input("Qual a velocidade do link(em Mbps)? "))

tempo_dw = tamanho/vel * 60

print(f'Tempo estimado para download: {tempo_dw:.2f} minutos.')

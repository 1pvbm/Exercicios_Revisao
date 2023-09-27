'''Escreva um algoritmo para ler o
número total de eleitores de um
município, o número de votos brancos,
nulos e válidos. Calcular e escrever o
percentual que cada um representa em
relação ao total de eleitores.'''
total_eleitores = int(input('Digite o total de Eleitores do Município : '))
votos_brancos = int(input('Digite o total de votos brancos: '))
votos_nulos = int(input('Digite o total de votos nulos: '))
votos_validos = int(input('Digite os votos válidos: '))
percentual_brancos = (votos_brancos / total_eleitores) * 100
percentual_nulos = (votos_nulos / total_eleitores) * 100
percentual_validos = (votos_validos / total_eleitores) * 100
print(f'Percentual de votos brancos: {percentual_brancos:.1f}%')
print(f'Percentual de votos nulos: {percentual_nulos:.1f}% ')
print(f'Percentual de votos válidos:{percentual_validos:.1f}% ')

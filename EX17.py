'''As maçãs custam R$ 1,30 cada se forem
compradas menos de uma dúzia, e R$ 1,00
se forem
compradas pelo menos 12. Escreva um
programa que leia o número de maçãs
compradas, calcule e
escreva o custo total da compra.'''
'''print('<MENU DE MAÇÃES>\nUnidade a R$ 1,30\nUnidade em dúzia a R$1,00')
menu = float(input('Quantas maçãs Deseja comprar ?'))
if menu >= 12:
    soma = menu * 1
    print(f'Você comprou com o preço da duzia (R$1,00), seu total: R$ {soma:.2f}')
else:
    soma = menu * 1.30
    print(f'Você comprou com o preço de unidade (R$1.30), seu total: R$ {soma:.2f}')
print('Programa encerrado.')'''
nmacas = int(input('Digite o número de maçãs: '))
precomaca = 1.0
if nmacas < 12:  # Se comprar pelo menos uma dúzia
    precomaca = 1.3
else:
    precomaca = 1.0
custo = nmacas * precomaca
print(f'O custo das maçãs é: R${custo:.2f}')
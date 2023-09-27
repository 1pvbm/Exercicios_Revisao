'''Crie um código que leia um número diferente de zero e diga se este número
é positivo ou negativo'''
num = float(input('Digite um número para saber se é positivo ou negativo: '))
if num == 0:
    print('<Programa encerrado>')
elif num > 0:
    print(f'{num} é um número POSITIVO')
else:
    print(f'{num} é um número NEGATIVO')



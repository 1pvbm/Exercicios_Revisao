#Crie um algoritmo que leia um número e diga se ele é par ou ímpar.
num = int(input('Digite um número para saber se é par ou ímpar: '))
if num % 2 == 0:
    print(f'O {num} é PAR.')
else:
    print(f'O {num} é ímpar.')

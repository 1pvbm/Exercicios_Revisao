'''Escreva um algoritmo para ler dois
valores (considere que não serão lidos
valores iguais) e escrevê-los em ordem
crescente'''
num1 = int(input('Digite um número: '))
num2 = int(input('Digite um número: '))
while num1 == num2:
    print('<os valores não podem ser iguais>')
    num1 = int(input('Digite um número: '))
    num2 = int(input('Digite um número: '))
if num1 > num2:
    print(f'A sequência crescente: {num1} , {num2}')
else:
    print(f'A sequência crescente: {num2}, {num1}')

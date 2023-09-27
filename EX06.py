'''Ler um valor e escrever a mensagem É MAIOR
QUE 10! se o valor lido for maior que 10, caso
contrário escrever NÃO É MAIOR QUE 10!'''
num = int(input('Digite um número para saber se é MAIOR ou MENOR que 10: '))
if num > 10:
    print(f'{num} é MAIOR que 10!')
elif num < 10:
    print(f'{num} é MENOR que 10!')
else:
    print('Programa Encerrado!')

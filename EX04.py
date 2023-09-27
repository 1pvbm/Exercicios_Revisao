#Crie um algoritmo que receba 3 números e informe qual o maior entre eles.
n1 = float(input('Digite 1ª Número: '))
n2 = float(input('Digite 2ª Número: '))
n3 = float(input('Digite 3ª Número: '))
if n1 > n2 > n3:
    print(f'O maior número foi: {n1}.')
elif n2 > n3:
    print(f'O maior número foi o {n2}.')
else:
    print(f'O maior número foi: {n3}')

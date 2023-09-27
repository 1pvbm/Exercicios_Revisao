'''Faça um código que receba 4
números e realize a soma deles e a
média entre eles. e mostre os
resultados.'''
soma = 0
for _ in range(4):
    num = float(input(f'Digite o seu {_ + 1}ª número: '))
    soma += num
MEDIA = soma / 4
print(f'A soma dos 4 números: {soma:.2f}\nA média da soma dos 4 números: {MEDIA:.2f}')

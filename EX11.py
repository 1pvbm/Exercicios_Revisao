'''Faça um algoritmo que leia a idade de
uma pessoa expressa em anos, meses e dias
e escreva a idade dessa pessoa expressa
apenas em dias. Considerar ano com 365
dias e mês com 30 dias.'''
ano = int(input('Digite a sua Idade (anos):  '))
mes = int(input('Digite a sua Idade (meses):  '))
dia = int(input('Digite a sua Idade (dias):  '))
idade_em_dias = ano * 365 + mes * 30 + dia
print(f'A quantidade de dias vividos em {ano} anos, {mes} meses e {dia} dias é : {idade_em_dias}')

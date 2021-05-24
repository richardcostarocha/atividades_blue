#01 - Utilizando estruturas condicionais faça um programa que pergunte ao usuário dois números e mostre:
   # A soma deles;
   # A multiplicação entre eles;
   # A divisão inteira deles;
   # Mostre na tela qual é o maior;
   # Verifique se o resultado da soma é par ou impar e mostre na tela;
   # Se a multiplicação entre eles for maior que 40, divida pelo resultado da divisão inteira e mostre o 
   # resultado na tela. Se não, mostre que a multiplicação não foi maior que 40.
from os import system
""" n1 = int(input('digite um valor: '))
n2 = int(input('digite outro valor: '))
print(f'a soma é: {n1+n2}')
print(f'a divisão entre {n1} com {n2} é: {n1/n2}')
if n1>n2:
   print(f'{n1} é maior que {n2}')
else:
   print(f'{n2} é maior que {n1}')
if (n1+n2)%2 == 0:
   print(f'a soma de {n1} com {n2} é par')
else:
   print(f'a soma de {n1} com {n2} é impar')
if (n1*n2)>40:
   if n1>n2:
      print(f'resultado: {(n1*n2)/(n1//n2)}')
   else:
      print(f'resultado: {(n1*n2)/(n2//n1)}')     
else:
   print(f'a muliplicação entre {n1} com {n2} não é maior que 40')
system('cls') """
#02 - Utilizando estruturas de repetição com variável de controle, faça um programa que receba uma string com 
# uma frase informada pelo usuário e conte quantas vezes aparece as vogais a,e,i,o,u e mostre na tela, 
# depois mostre na tela essa mesma frase sem nenhuma vogal.
""" frase = str(input('digite uma frase: ')).lower() 
cont = 0
for i in frase:
   if i in 'aeiou':
      cont +=1
print(f'na frase tem {cont} vogais')
for i in 'aeiou':
   frase = frase.replace(i,' ')
print(f'a frase sem as vogas fica: {frase}') """
#03 - Utilizando estruturas de repetição com teste lógico, faça um programa que peça uma senha para iniciar
#  seu processamento, só deixe o usuário continuar se a senha estiver correta,
#  após entrar dê boas vindas a seu usuário e apresente a ele o jogo da advinhação,
#  onde o computador vai “pensar” em um número entre 0 e 10.
#  O jogador vai tentar adivinhar qual número foi escolhido até acertar,
#  a cada palpite do usuário diga a ele se o número escolhido pelo computador é maior ou menor ao que ele palpitou,
#  no final mostre quantos palpites foram necessários para vencer.
""" from random import randint
senha = 'richard gostosão'
comp = randint(0,10)
erro = 0
senhateste = ''
senhateste = str(input('digite a senha: '))
while senhateste != senha:
   system('cls')
   senhateste = str(input('senha invalida!\ndica: "criador gostosão"\ndigite a senha: '))
print('\33[33;41m')
print('============')
print('|Bem Vindo!|')
print('============')
print('\33[m')
print('\33[7m   ')
usuario = int(input('tente adivinhar qual foi o numero que o pc escolheu(dica: foi um numero de 0 a 10): '))
while usuario != comp:
   erro += 1
   if usuario > comp:
      print('seu numero foi maior!')
   else:
      print('seu numero foi menor!')
   usuario = int(input('vc errou, tente novamente: '))
print(f'vc precisou de {erro} vezes para acertar o numero {comp}')
"""
#04 - Utilizando funções e listas faça um programa que receba uma data no formato DD/MM/AAAA e devolva uma string 
# no formato DD de mesPorExtenso de AAAA. Opcional: valide a data e retorne 'data inválida' caso a data seja 
# inválida.
""" data = str(input('data(dd/mm/aaaa):  '))
def dataAjustada(data):
   dia,mes,ano = data.split('/')
   mesPorExtenso = ('Janeiro','Fevereiro','Março','Abril','Maio','Junho','Julho','Agosto','Setembro','Outubro','Novenbro','Dezembro')
   if mes == '01':
      mes = mesPorExtenso[0]
   elif mes == '02':
      mes = mesPorExtenso[1]
   elif mes == '03':
      mes = mesPorExtenso[2]
   elif mes == '04':
      mes = mesPorExtenso[3]
   elif mes == '05':
      mes = mesPorExtenso[4]
   elif mes == '06':
      mes = mesPorExtenso[5]
   elif mes == '07':
      mes = mesPorExtenso[6]
   elif mes == '08':
      mes = mesPorExtenso[7]
   elif mes == '09':
      mes = mesPorExtenso[8]
   elif mes == '10':
      mes = mesPorExtenso[9]
   elif mes == '11':
      mes = mesPorExtenso[10]
   elif mes == '12':
      mes = mesPorExtenso[11]     
   return (dia,mes,ano)
dia,mes,ano = dataAjustada(data)
print(f'a data digitada é: {dia}/{mes}/{ano}') """
#05 - Refatore o exercício 2, para que uma função receba a frase, faça todo o tratamento necessário e retorne o
#  resultado. Depois mostre na tela o resultado e a quantidade de letras foram retiradas da frase original.
""" frase = str(input('digite uma frase: ')).lower() 
contA = contE = contI = contO = contU = cont = 0
for i in frase:
   if i in 'aeiou':
      cont += 1
   if i == 'a':
      contA += 1
   elif i == 'e':
      contE += 1
   elif i == 'i':
      contI += 1 
   elif i == 'o':
      contO += 1
   elif i == 'u':
      contU += 1   
print(f'na frase tem {cont} vogais')
for i in 'aeiou':
   frase = frase.replace(i,' ')
print(f'a frase sem as vogas fica: {frase}')
print(f'foram retiradas {contA} vogais A da frase')
print(f'foram retiradas {contE} vogais E da frase')
print(f'foram retiradas {contI} vogais I da frase')
print(f'foram retiradas {contO} vogais O da frase')
print(f'foram retiradas {contU} vogais U da frase') """
#06 - Utilizando listas faça um programa que faça 5 perguntas para uma pessoa sobre um crime. As perguntas são:
   # "Telefonou para a vítima?"
   # "Esteve no local do crime?"
   # "Mora perto da vítima?"
   # "Devia para a vítima?"
   # "Já trabalhou com a vítima?" 
# O programa deve no final emitir uma classificação sobre a participação da pessoa no crime. 
   # Se a pessoa responder positivamente a 2 questões ela deve ser classificada como "Suspeita",
   # Entre 3 e 4 como "Cúmplice" e 5 como "Assassino". 
   # Caso contrário, ele será classificado como "Inocente".
""" resporta = list()
resporta.append(input('Telefonou para a vítima? ').lower().strip()[0])
resporta.append(input('Esteve no local do crime? ').lower().strip()[0])
resporta.append(input('Mora perto da vítima? ').lower().strip()[0])
resporta.append(input('Devia para a vítima? ').lower().strip()[0])
resporta.append(input('Já trabalhou com a vítima? ').lower().strip()[0])

if resporta.count('s') == 2:
    print('Suspeita')
elif resporta.count('s') == 3 or resporta.count('s') == 4:
    print('Cúmplice')
elif resporta.count('s') == 5:
    print('Assassino')
else:
    print('Inocente')
 """
#07 - Crie um programa onde o usuário possa digitar sete valores numéricos e cadastre-os em uma lista única que
#  mantenha separados os valores pares e ímpares. No final, mostre os valores pares e ímpares em ordem crescente.
""" valor = [list(),list()]
for i in range(7):
   alx = 0
   alx =int(input('digite um valor: '))
   if alx % 2 == 0:
      valor[0].append(alx)
   else:
      valor[1].append(alx)
valor[0].sort()
valor[1].sort()
print(f'os numers pares em ordem crescente é: {valor[0]}')
print(f'os numers inpares em ordem crescente é: {valor[1]}')
 """
#08 - Crie um programa que leia nome, ano de nascimento e carteira de trabalho e cadastre-os (com idade) 
# em um dicionário. Se por acaso a CTPS for diferente de 0, o dicionário receberá também o ano de contratação 
# e o salário. Calcule e acrescente , além da idade, com quantos anos a pessoa vai se aposentar.
# Considere que o trabalhador deve contribuir por 35 anos para se aposentar.
""" from datetime import date
anoAtual = date.today().year
funcionario = dict()
funcionario['nome'] = str(input('nome: '))
nascimento = int(input('ano de nascimento: '))
idade = anoAtual - nascimento
funcionario['idade'] = idade
funcionario['CTPS'] = int(input('carteira de trabalho: '))
if funcionario['CTPS'] != 0:
    contratação = int(input('ano de contratação: '))
    anoDeContratação = anoAtual - contratação
    funcionario['anoDeContratação'] = anoDeContratação
    funcionario['salario'] = float(input('salario: '))
    aposentadoria = 35 - funcionario.get('anoDeContratação')
    aposentado = idade + aposentadoria
    funcionario['aposentadoria'] = aposentado
print(funcionario) """
'''
Escreva um programa que, ao iniciar, gera um valor aleatório de 1 a 10 e permite que o usuário chute um número até que o valor aleatório gerado no início do programa seja chutado corretamente.

O programa deve informar se o chute foi acima, abaixo ou igual ao valor aleatório gerado no início do programa.

Metódo 5Q's para montar um algoritmo:

Analise criticamente o problema e descubra:
(Tente explicar este problema para você mesmo em voz alta e peça mais informações/investigue mais até você compreender completamente o problema.)

1. Quais são os dados de entrada necessários?
# random_number, number
2. O que devo fazer com estes dados?
# comparar os valores e retornar se o valor chutado foi igual, maior ou menor que o valor gerado
3. Quais são as restrições deste problema?
# O valor aleatorio deve ser de 1 a 10
4. Qual o resultado esperado?
# O programa deve retornar se o chute foi acima, abaixo ou igual ao valor gerado
5. Qual é a sequência de passos para resolver este problema?

input random_number de 1 a 10
input number
if number > random_number
  print('Chute mais baixo!')
elif number < random_number
  print('Chute mais alto!')
else
  print('Acertou!')
'''
import random

random_number = random.randint(1, 10)
acertou = False
while acertou == False:
  number = int(input('Chute um número: '))
  if number > random_number:
    print('Chute mais baixo!')
  elif number < random_number:
    print('Chute mais alto!')
  else:
    print('Acertou!')
'''
Crie um programa que rece um número e imprima seu fatorial.

Método 5Q's para montar um algoritmo:

Analise criticamente o problema e descubra:
(Tente explicar este problema para você mesmo em voz alta e peça mais informações/investigue mais até você compreender completamente o problema.)

1. Quais são os dados de entrada necessários?
numero
2. O que devo fazer com estes dados?
calcular o fatorial do numero passado e exibi-lo na tela
3. Quais são as restrições deste problema?
não é possível calcular o fatorial de um número negativo e precisa ser inteiro
4. Qual o resultado esperado?
fatorial do numero passado
5. Qual é a sequência de passos para resolver este problema?

input numero
if numero > 0
if numero = inteiro
fatorial = 1
loop de 1 a numero
  fatorial = fatorial * numero
print(fatorial)
'''
number = int(input('Digite um número: '))
if number > 0:
  factorial = 1
  for i in range(1, number + 1):
    factorial = factorial * i
  print(factorial)
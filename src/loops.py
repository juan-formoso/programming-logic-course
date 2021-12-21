# Laços de Repetição + Listas

for palavra in range(1,4):
  print('carregando')
'''
for item in array
  expressão
'''
for item in range(1,20):
  print(item)
for item in range(1,20,2):
  print(item)

names = ['João', 'Maria', 'José', 'Pedro']
for name in names:
  print(name)
'''
input numero_maximo
valor_inicial = 1
loop de valor_inicial a numero_maximo
  print valor
'''
valor_maximo = int(input('Digite um valor maximo: '))
valor_inicial = 1
for numero in range(valor_inicial, valor_maximo + 1):
  print(numero)
# Coleções(listas)
preco_1 = 10
preco_2 = 20
preco_3 = 30
# Lista
precos = [10, 20, 30]
# 0, 1, 2
print(precos.index[0])
print(precos.index(200))
# Lista
diversidades = [15, 'Johnatan', True]
print(diversidades[0])
print(diversidades[1])
print(diversidades[2])
# Laços em iteráveis.
for preco in precos:
  print(preco)

'''
# Exemplo 5 - Some os valores
Dados um coleçaõ de dados "idades" [10, 20, 30, 40, 50] imprima na tela a soma destes valores.

idades = [10, 20, 30, 40, 50]
soma = 0
loop idade em idades
  soma = total + idade
print soma
'''
idades = [10, 20, 30, 40, 50]
total = 0
for idade in idades:
  total = total + idade
print(total)
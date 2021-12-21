# Variaveis
velocidade_internet = 10
print(velocidade_internet)
nota_filme = 8.5 # float
# Numeros
# Valores booleanos
esta_aberto = False
# Strings
nome_do_curso = "Logica de Programacao"

# Como variaveis seriam usadas em um programa real?
# Problema 1 - Valor por Hora
# Escreva um programa que retorna o valor de um funcionario com base no seu salário mensal e horas trabalhadas por mes.
'''
input salario_mensal
input horas_trabalhadas
valor_hora = salario_mensal /horas_trabalhadas
print valor_hora
'''
salario_mensal = input('Digite o salário mensal: ')
horas_trabalhadas = input('Digite as horas trabalhadas: ')
valor_hora = int(salario_mensal) / int(horas_trabalhadas)
print(valor_hora)
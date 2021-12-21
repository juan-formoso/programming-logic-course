# Condicionais
# if, elif, else
'''
E ae jovem, bora dar uma saída hoje?
Se eu terminar meu trabalho aqui, eu consigo.
'''
trabalho_terminado = True
if trabalho_terminado == True:
  print('Opa, bora dar um rolê!')
else:
  print('Não vai dar, vou ficar ocupado.')

'''
Ei, você consegue me ajudar a mover essas coisas lá pra baixo?
Se eu estiver livre sim, senão pede pra mamãe.
'''
estou_livre = False
if estou_livre == True:
  print('Ok, posso te ajudar!')
else:
  print('Não posso te ajudar, peça ajuda da mamãe.')

'''
Eu cheguei atrasado, mas você consegue me ajudar a fazer o trabalho?
Se esse não for seu terceiro atraso, então posso sim, senão... Sinto muito.
'''
atrasos = 2
if atrasos >= 3:
  print('Sinto muito, mas não posso te ajudar.')
elif atrasos == 1:
  print('Ok, posso te ajudar.')
elif atrasos == 2:
  print('Ok, posso te ajudar.')
else:
  print('Posso te ajudar.')

# Encontre o maior entre 2 números
'''
input primeiro_valor
input segundo_valor
if primeiro_valor > segundo_valor:
  print o primeiro_valor é maior
else:
  print o segundo_valor é maior
'''
primeiro_valor = input('Digite o primeiro valor: ')
segundo_valor = input('Digite o segundo valor: ')

if int(primeiro_valor) > int(segundo_valor):
  print('O primeiro valor é maior.')
else:
  print('O segundo valor é maior.')
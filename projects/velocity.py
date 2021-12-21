'''
Projeto - Medidor de Velocidade

Levando em consideração a velocidade máxima permitida de 80km em uma determinada rua. Crie um programa que recebe do usuário um valor que representa a velocidade e com base nessa velocidade diga se ele tomou um multa leve, grave ou gravíssima. Levando em consideração que se a pessoa estiver abaixo da velocidade máxima seu programa deve exibir "não houve multa", caso esteja até 10km acima, deve exibir: "levou multa leve", caso esteja entre 11 a 20km acima da velocidade máxima, exibir: "levou multa grave", e caso esteja acima de 20km acima da velocidade máxima, exiba: "levou multa gravíssima".

Analise criticamente o problema e descubra:
(Tente explicar este problema para você mesmo em voz alta e peça mais informações/investigue mais até você compreender completamente o problema.)

1. Quais são os dados de entrada necessários?
# velocidade
2. O que devo fazer com estes dados?
# comparar os valores de velocidade e retornar se a levou multa e caso tenha levado, se esta foi leve, grave ou gravíssima
3. Quais são as restrições deste problema?
# nenhuma
4. Qual o resultado esperado?
# o resultado esperado é exibir a mensagem que corresponde ao nível de multa que a pessoa levou (deve exibir: "levou multa leve", caso esteja entre 11 a 20km acima da velocidade máxima, exibir: "levou multa grave", e caso esteja acima de 20km acima da velocidade máxima, exiba: "levou multa gravíssima".)
5. Qual é a sequência de passos para resolver este problema?

input velocidade
velocidade_max = 80
if velocidade <= velocidade_max:
  print('Não houve multa')
if velocidade > velocidade_max and velocidade <= velocidade_max 10:
  print('Levou multa leve')
if velocidade > velocidade_max + 11 and velocidade <= velocidade_max + 20:
  print('Levou multa grave')
if velocidade > velocidade_max + 20 :
  print('Levou multa gravíssima')
'''
velocidade = int(input('Digite a velocidade: '))
velocidade_max = 80
if velocidade <= velocidade_max:
  print('Não houve multa')
elif velocidade > velocidade_max and velocidade <= velocidade_max + 10:
  print('Levou multa leve')
elif velocidade > velocidade_max + 11 and velocidade <= velocidade_max + 20:
  print('Levou multa grave')
elif velocidade > velocidade_max + 20:
  print('Levou multa gravíssima')
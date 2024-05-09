# calculo 4

import math

n = 2
resultado = 0

while n < 10000:
  resultado += 1 / (n * math.log(n, math.e)**2)
  print(resultado)
  n += 1
  
resposta = "Nao converge, pois o valor continua infinitamente subindo"

print(resposta)
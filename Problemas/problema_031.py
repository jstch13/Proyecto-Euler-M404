#Problema 031 - Suma de Monedas
#Enunciado: https://projecteuler.net/problem=31
#Nivel de Dificultad: d = 2
#Puntos: p(d,n) = 6
#Tiempo observado en Colab (CPU): 0.000000 s
#Estrategia: hallar las combinaciones lienales que resulvan el problema

n_i = float(input("Valor en Euros el cual se desea completar con monedas: "))

#funcion que halla las combinaciones lineales usando una lista de valores que podrian coincidir
def combinacioneslineales(eu):
  n_m = int(eu * 100)
  monedas = [1, 2, 5, 10, 20, 50, 100, 200]
  CL = [0] * (n_m + 1)
  CL[0] = (1)
#y si pasan (suman 100+n_i) lo agrega como un caso que sirve y va sumando cuantos cumplen
  for moneda in monedas:
    for i in range(moneda, n_m + 1):
      CL[i] += CL[i - moneda]

  return CL[n_m]

total = combinacioneslineales(n_i)

print(f"Total de combinaciones encontradas: {total}")
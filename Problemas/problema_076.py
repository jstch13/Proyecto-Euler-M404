#Problema 076 - Sumas de 100
#Enunciado: https://projecteuler.net/problem=76
#Nivel de Dificultad: d = 2
#Puntos: p(d,n) = 6
#Tiempo observado en Colab (CPU): 0.000000 s
#Estrategia: Usando la definicion de numeros pentagonales y con ellos halar particiiones
#Pues si pensamos que podemos hacer subgrupos de los cien 1`s y sumarlos estos daran las particiones
#como tiene que ser al menos 2, le resto la cantidad de hacer un grupo

n_i = int(input("Número que se desea encontrar sus posible sumas con dos o mas numeros: "))

#Definimos una funcion que cuenta los subgrupos a partir de el teorema de los numeros pentagonales

def subgrupos(n):
  sb = [0] * (n + 1)
  sb[0] = 1
#definimos una forma de hallar los numeros pemtagonales generalizados por medio de un bucle que recorre de 1 a n
  for i in range(1, n + 1):
    j = 1
    signo = 1
    while True:
      pentagonal1 = j * (3 * j - 1) // 2
      pentagonal2 = j * (3 * j + 1) // 2

      if pentagonal1 > i:
        break
#la recurrencia que descubrio euler 
      sb[i] += signo * sb[i - pentagonal1]

      if pentagonal2 <= i:
        sb[i] += signo * sb[i - pentagonal2]
#se encuentra el signo de cada valor (2 positivos, 2 negativos)
      j += 1
      signo = -signo

  return sb[n]

#subgrupos de n, menos la condicion de ser al menos 2 numeros
resultado = subgrupos(n_i) - 1

print(f"Total de formas de sumar 100 con al menos dos números: "f" {resultado}")
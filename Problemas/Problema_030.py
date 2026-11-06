#Problema 030 - Suma de Potencias Quinticas
#Enunciado: https://projecteuler.net/problem=30
#Nivel de Dificultad: d = 0
#Puntos: p(d,n) = 1
#Tiempo observado en Colab (CPU): 0.000000 s
#Estrategia: Reducir el margen de busqueda sabiendo que la suma de las potencias quinticas de los digitos de un numero
#es como maximo la cantidad de digitos por 9 elevado a la 5
import time

def solve_problema():
    inicio = time.perf_counter()
    
#Precalculamos las quintas potencias del 0 al 9 para no estarlas calculando
    potencias_5 = [i**5 for i in range(10)]
    
    total_suma = 0
    
#El límite superior matemático es 6 * (9^5) = 354,294, pues con siete es imposible
#Comenzamos desde 2 ya que el 1 no se considera una suma de potencias válida
    for num in range(2, 354295):
        suma = 0
        temp = num
        
#ahora separamos los digitos del numero
        while temp > 0:
            suma += potencias_5[temp % 10]
            temp //= 10
            
#Si la suma de las quintas potencias es igual al número original se contabiliza
        if suma == num:
            total_suma += num
            
    fin = time.perf_counter()
    
    print(f"Respuesta: {total_suma}")
    print(f"Tiempo observado en Colab (CPU): {fin - inicio:.6f} s")
    
    return total_suma

if __name__ == "__main__":
    solve_problema()
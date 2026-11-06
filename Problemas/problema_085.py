#Problema 085  - Contando Rectangulos
#Enunciado: https://projecteuler.net/problem=85
#Nivel de Dificultad: d = 3
#Puntos: p(d,n) = 8
#Tiempo observado en Colab (CPU): 0.000000 s
#Estrategia: sabiendo que existe una formula para calcular los rectangulos de una cuadrucla de axb, y partir el caso en el que a=b=a+1=b+1,
# pueda existir y redondeando para abajo e ir probando valores hallar el minimo entre la resta de estas

k = 4*int(input("Ingrese el valor que desea aproximar sus rectangulos: "))

#la formula conocida de rectangulos de una cuadricula de axb es (a)(a+1)(b)(b+1)/4
#por lo quue al multiplicar x4 se tendria que parecer los mas posible a  veces el numero que deseamos
ad = int(k**(1/4))+1

#asumiendo que fuesen 4 valores iguales seria la raiz cuartica, con lo que tendria que ser menor
#a esta, y estara entre 1 y la raiz cuartica
#asumamos b = raiz(ad/a+a+1) osea b = b+1 aprox
resultados = []
for a in range (1, ad):
    b = int((k**(1/2))/((a*(a+1))**(1/2)))
    x_i = abs((b)*(b+1)*(a)*(a+1)-k)
    resultados.append((a, b, x_i))

#solo buscamos el x_i mas pequeño y esa sera la menor diferencia
mejor_resultado = min(resultados, key=lambda item: item[2])

mejor_a = mejor_resultado[0]
mejor_b = mejor_resultado[1]
mejor_x_i = mejor_resultado[2]

#calculamos el area
area = (mejor_a*mejor_b)

print(f"La mejor combinación es: a = {mejor_a}, b = {mejor_b} (con un x_i de {mejor_x_i}), lo que tiene un área de {area}")
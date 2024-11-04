#Escribir un programa que pregunte por una muestra de números, separados por comas, los guarde en una lista y muestre por pantalla su media y desviación típica.
Numero = input("Escriba una muestra de numero separados por coma ")
Numero = Numero.split(',')
n = len(Numero)
for i in range(n):
    Numero[i] = int(Numero[i])
lista = tuple(Numero)
suma = 0
resto = 0
for i in lista:
    suma += i
    resto += i**2
x = suma/n
a = (resto/n-x**2)**(1/2)
print('La media es', x, ', y la desviación típica es', a)
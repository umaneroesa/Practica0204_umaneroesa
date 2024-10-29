#Escribir un programa que pregunte al usuario los números ganadores de la lotería primitiva, los almacene en una lista y los muestre por pantalla ordenados de menor a mayor.
lista =[]
a = 0
while 5 > a:
    lista.append(input("Dime los numeros ganadores de la primitiva "))
    a= a+1
lista.sort()
print(lista)
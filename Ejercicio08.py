#Escribir un programa que pida al usuario una palabra y muestre por pantalla si es un palíndromo.
palabra= input("Dime una palabra ")
alabra = palabra
palabra=list(palabra)
alabra=list(alabra)
alabra.reverse()
if palabra == alabra:
    print("Palindromo")
else:
    print("No es palindromo")
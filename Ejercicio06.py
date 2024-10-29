#Escribir un programa que almacene las asignaturas de un curso (por ejemplo Matemáticas, Física, Química, Historia y Lengua) en una lista, pregunte al usuario la nota que ha sacado en cada asignatura y elimine de la lista las asignaturas aprobadas. Al final el programa debe mostrar por pantalla las asignaturas que el usuario tiene que repetir.
Asignaturas=["Matematicas","Fisica","Quimica","Historia","Lengua"]
Repite=[]
for i in Asignaturas:
    nota = float(input("Nota de la asignatura "+ i + " "))
    if nota<5:
        Repite.append(i)
print("Tienes que repetir las siguientes asifnaturas " + str(Repite))
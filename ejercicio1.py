#Autor: k.K

#Este es un comentario de una línea

#Este es un comentario
#que ocupa varias lineas
""""
Este es otro es otro ejemplo
de comentario multilínea
"""

'''
ESte es otro ejemplo de comentario
multilinea
'''
entero = 42 
decimal = 3.1416 #Numeros decimales (float)
logico = True #Boolean 
nombre = "Juan" #String

print(type (entero))
print (type (decimal))
print(type(logico))
print (type(nombre))
#Declara variables que almacene su nombre, estatura, apellido 
# pater, materno, y edad

nombre = "Jose de la Cruz"
Apellido_p = "Povedano"
Apellido_m = 'Esponda'
edad = 19
estatura = 1.62
print(nombre)
print(Apellido_m)
print(Apellido_p)
print(edad)
print(estatura)


nombre_Materia = 'Programacion'
#se inicia desde 0, P es igual a 0
print(nombre_Materia[0])
print(nombre_Materia[-4])
print(nombre_Materia[0:6])

calificaciones = [8.5,9.0,7.5,10.0]
#append sirve para insertar un número sin modificar la lista
calificaciones.append(9.5)
calificaciones[0] = 8.0
print(calificaciones)

#tuple - inmutable
coordenadas = (19.4326, -99.1332)
print(coordenadas[0])

#dict - clave: valor
alumno = {'nombre': "Jose", "edad": 28, "promedio" : 10}
print(alumno['nombre'])
alumno['promedio'] = 9.6
print(alumno)

#Crea un diccionario con tus datos: nombre, edad y materia favorita. 
# Imprimite solo tu nombre accediendo  ala clave correcta.
mascara = {'ser': 'povedano', 'edad': 20, 'materia_fav': "literatura"}
print(mascara['ser'])
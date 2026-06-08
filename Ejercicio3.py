#Identificadores y variables
#variables con snake_case

#Quiero obtener el nombre de un alumno, como pdebo definir mi   
# identificador?
nombre_alumno = "Jose Povedano"
edad_alumno = 28
promedio_final = 9.5

#Constantes con SCREAMING SNAKE CASE
TASA_IVA = 0.16
#CALIFICACION_MINIMA = 7.0
#PESO_PARCIAL = 0.20
PI = 3.1416
GRAVEDAD_PLANETA = 9.84
CAPACIDAD_MAXIMA_SALON = 25

#Tipado dinamico - la variable cambia de tipo
dato = 100
print(type(dato))
dato = 'cien'
print(type(dato))

#Uso de constante en un calculo
precio_base = 500.0
precio_final = precio_base * (1 + TASA_IVA)
print(f'Precio con IVA: ${precio_final:.2f}')
#la f es para que se realize la conversion, y el 2f para limitar los decimales

#Define 3 constantes: PESO_PARCIAL = 0.20, PESO_PROYECYO=0.40 Y CALIFICACION_MINIMA
#=6.0. Luego crea 4 variables con calificaciones y calcula el promedio usando las
#constantes. Imprime si el alumno aprobo o reprobo.
PESO_PARCIAL = 0.20
PESO_PROYECTO = 0.40
CALIFICACION_MINIMA = 6.0

calificacion1 = 5
calificacion2 = 5
calificacion3 = 5
calificacion4 = 5
suma = (calificacion1 + calificacion2 + calificacion3 + calificacion4)
promedio = ((suma / 4))
print('Aprobado ' if promedio >= CALIFICACION_MINIMA else 'Reprobado')

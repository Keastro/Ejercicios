#-Casting basico
#Implicita: int + float = float automaticamente
resultado = 5 + 2.0
print(resultado)
print(type(resultado))

#Emplicita; str a int
texto_numero = '42'
numer_real = int(texto_numero)
print(numer_real + 8)

#Explicita: int a str para concatenar

edad = 28
mensaje = 'Hola, soy Juan y mi edad es ' + str(edad)
print(mensaje)

#float a int
precio = 9.99
print(int(precio))

numero = 7.99
redondeado = round(numero)
print(redondeado)

#Simularemos input con variables fijas
dato_usuario = '25'
print(type(dato_usuario))
#print(dato_usuario + 5)

edad_correcta = int(dato_usuario)
print(edad_correcta + 5)

#Patron correcto para entreda de datos
#edad = int(input('Ingresa tu edad '))

#Escribe un programa que pida al usuario su nombre (str) y su año de 
# año de nacimiento (int). Calcula e imprime su edad aproximada restando
# el año actual.
name = input("Ingresa tu nombre ")
fecha = int(input('Ingresa tu año de nacimiento '))
num_real= int(fecha)
calculo = print('Su edad es ', 2026 - fecha)
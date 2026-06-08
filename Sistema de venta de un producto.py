#Sistema de venta de un producto

nombre = input('Cual es tu nombre? ')
nombre_producto = input('Como se llama el producto que quiere? ')
Precio_unitario = float(input('Cuanto cuesta? '))
cantidad = int(input('Cuantos quiere? '))
IVA = 0.16
DESCUENTO = 0.10

print('TIPOS DE DATOS')
print(type(cantidad))
print(type(IVA))
print(type(nombre))


print("|Ticket|")

resumen = print("Compra a nombre de ", nombre, "Quien compro un total de ", cantidad, nombre_producto)
precio_iva = (Precio_unitario*IVA * cantidad)
print('Este es es su IVA', precio_iva)
aplicacion_descuento = Precio_unitario * DESCUENTO *cantidad
print('Este es su descuento', aplicacion_descuento)


Precio_total = (Precio_unitario*cantidad + precio_iva - aplicacion_descuento)


print('Total a pagar con descuento e IVA', + Precio_total)
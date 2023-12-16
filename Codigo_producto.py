#Una empresa proveedora de alimentos, necesita generar un código para cada producto, según las
#siguientes reglas:

#-El primer y segundo carácter, deben ser dos consonantes en mayúsculas del nombre del producto.
#-El tercer carácter, debe ser una vocal aleatoria en minúscula del nombre del producto.
#-Luego, un número aleatorio entre el 100 y el 999.
#-El último carácter, debe ser "*" si la cantidad de caracteres del nombre del producto es impar,
#y en caso contrario, debe ser un "#"

#Se nos pide realizar un programa que, dado el nombre de un producto, genere su respectivo código.
#Por ejemplo, si el usuario ingresa: "tomates triturados", un código posible sería: TMe853#.

import random

producto=input("por favor, ingrese el nombre del producto: ")
consonantes="bcdfghjklmnñpqrstvwxyzBCDFGHJKLMNÑPQRSTVWXYZ"
vocales="aeiouAEIOU"
con_producto=""
voc_producto=""
código=""

#Primero, separamos el producto en consonantes y vocales
for char in producto:
    if char in consonantes:
        con_producto+=char
    else:
        voc_producto+=char

#ahora, tomamos las dos consonantes para ponerlas en el código
c=1
for char in con_producto:
    if c<=2:
        código+=char.upper()
    c+=1
#print(código) #primer print, solo para verificar que el código tome las dos vocales.
    
#ahora, agrego una vocal aleatoria
vocal=random.choice(voc_producto)
código+=vocal.lower()
#print(código) #otro print para verificar.

#agregamos un número random entre 100 y 999
número=random.randint(100, 999)
código+=str(número)
#print(código) #print para verificar.

#por último, agregamos "*" o "#", según la cantidad de carateres.
cant_caracteres=len(producto)
if cant_caracteres%2!=0:
    código+="*"
else:
    código+="#"
print(código) #este print es el importante, y el único que debe quedar.
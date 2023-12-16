#Una empresa proveedora de alimentos, necesita generar un código para cada producto, según las
#siguientes reglas:

#-El primer y segundo carácter, deben ser dos consonantes en mayúsculas del nombre del producto.
#-El tercer carácter, debe ser una vocal aleatoria en minúscula del nombre del producto.
#-Luego, un número aleatorio entre el 100 y el 999.
#-El último carácter, debe ser "*" si la cantidad de caracteres del nombre del producto es impar,
#y en caso contrario, debe ser un "#"

#Se nos pide realizar un programa que, dado el nombre de un producto, genere su respectivo código.
#Por ejemplo, si el usuario ingresa: "tomates triturados", un código posible sería: TMe853*.

producto=input("por favor, ingrese el nombre del producto: ")
consonantes="bcdfghjklmnñpqrstvwxyzBCDFGHJKLMNÑPQRSTVWXYZ"
vocales="aeiouAEIOU"
con_producto=""
voc_producto=""
código=""

#Primero, separamos el producto en consonantes y vocales
for char in palabra:
    if char in consonantes:
        con_producto+=char
    else:
        voc_producto+=char
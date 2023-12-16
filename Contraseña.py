#Hacer un programa, donde el usuario deba ingresar una contraseña. Tiene hasta 3 intentos.
contraseña_guardada="Boquitapasión"
contraseña=input("Por favor, ingrese su contraseña: ")
flag=True
c=1

if contraseña==contraseña_guardada:
    print("Bienvenido al sistema.")
else:
    while c<=3 and flag:
        contraseña=input("Contraseña incorrecta, intentelo de nuevo: ")
        if contraseña_guardada==contraseña:
            flag=False
        c+=1
    if flag==False:
        print("Bienvenido al sistema.")
    else:
        print("Demasiados intentos. Intentelo más tarde.")
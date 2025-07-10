#Tipos de datos fundamentales y operadores
#Tipos de Datos básicos 
#Enteros
edad = 30
print("edad:", edad, "|Tipo", type(edad))

#Float o flotantes
precio = 19.99
print("El precio es:", precio, "| Tipo", type(precio))

#Boleanos lógicos o condiciónantes , si tal condición se cumple es verdadero o sino se cumple la condición esfalso
activo = True
print("Activo es:", activo, "| Tipo", type(activo))

#Cadenas de texto (String)

nombre = "Jaqueline" 
print("Nombre", nombre, "| Tipo" , type(nombre))

#Variables y nombre válidos
#Asinación simple
nombre_usuario = "Jaqueline"
edad_usuario = 30

#Nombres válidos
nombre_completo = "Jaqueline Adriano"
numero1 = 35

#Tip: usar nombres descriptivos y en minúsculas con guión bajo

##Operadores aritméticos
#Operadores aritméticos
a = 20
b = 500
c = 25
print("suma: ", a + b + c)
print("resta: ", a - b - c)
print("multiplicación: ", a*b*c)
print("División: ", a / b / c) 
print("División Entera: ", a // b // c)
print("Módulo: ", a % b)
print("Potencia: ", a ** b )

##Operadores de Comparación 
# se manejan vaores boleanos 
x = 7 
y = 5

print("El resultado de: ", x == y)
print("Es diferente a", x != y)
print("Mayor que", x > y)
print("Menor que", x < y)
print("Mayor o igual que", x >= y)
print("Menor o igual que", x <= y)

#Operadores de asignación
#Es cuando se van a incrementar o dismuinuir una variable
contador = 5

contador  += 2 #Equivalente a contador  = contador + 2
print("+=: ", contador)

contador  *= 3 #Equivalente a contador  = contador * 3
print("*=: ", contador)

contador  -= 4 #Equivalente a contador  = contador - 4
print("-=: ", contador)

contador  /= 2 #Equivalente a contador  = contador / 2
print("/=: ", contador)
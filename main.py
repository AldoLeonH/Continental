# Refresh de Hola Mundo;
# print("Refresh of Python")
# print("Resfresh de Python 2")

# Guardar texto en una variable
texto="Refresh de pyhton"
# print(texto)

#Guardar texto y numeros en variables
nombre= "aldo leon"
altura= "170 cm"
year= 1997

#Concatenación de variables
# print(f"Esto es un {texto} soy {nombre} mi estatura es de {altura} y naci en el año {str(year)}")
# Nombre = input("¿Cual es tu nombre? ")
# print(f"Hola {Nombre} este es un {texto}")

# # Condicionales
# altra = input("¿Cuánto mides mi amigo?")
# altra=int(altra)
# if altra<=150:
#     print("Eres una persona chaparrita")
# else:
#     print("You are tall my pal")

#Funciones
# def showAge():
#     edad=int(input("¿Que edad tienes?"))
#     if edad>=18:
#         print("Tu eres una persona mayor de edad")
#     else:
#         print(f"Tu no eres mayor de edad, tu edad esta por debajo de los 18 años, tu solamente tienes {edad} años")
#  showAge(); llamando a la funcion para que hace lo que esta adentro de ella

def showAge(edad):
    if edad>=18:
        print("Tu eres una persona mayor de edad")
    else:
        print(f"Tu no eres mayor de edad, tu edad esta por debajo de los 18 años, tu solamente tienes {edad} años")

# tuEdad=int(input("¿Cuál es tu edad amigo?"))
#showAge(tuEdad); Para activar la funcion debemos de quitar el comentario

#Listas

personas=["Viricita","Aldo", "Arcelia"]
# print(personas)
# print(personas[1])
# print(personas[2])
# print(personas[0])

for personas in personas:
    print(f" - {personas}")



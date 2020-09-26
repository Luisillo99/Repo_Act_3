#Actividad 3 - Sabores de Helado - Luis Enrique Preciado Muñiz

import Funciones as fun

sabores=[]
gusto=[]
print("Ingresa los sabores de Helado que más te gusten")
for i in range(5):
    sabores.append(input(f"{i+1}.- "))
nombre=input("Ingresa tu nombre: ")
apell=input("Ingresa tu apellido: ")

gusto = fun.ingresar_dat(sabores)
sabores = fun.ordenar_dat(nombre,apell,gusto,sabores)
fun.mostrar_dat(sabores)
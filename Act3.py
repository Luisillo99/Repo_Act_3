#Actividad 3 - Sabores de Helado - Luis Enrique Preciado Muñiz

import Funciones as fun

sabores=["Chocolate","Vainilla","Fresa","Pistache","Napolitano"]
gusto=[]
nombre=input("Ingresa tu nombre: ")
apell=input("Ingresa tu apellido: ")

gusto = fun.ingresar_dat(sabores)
sabores = fun.ordenar_dat(nombre,apell,gusto,sabores)
fun.mostrar_dat(sabores)
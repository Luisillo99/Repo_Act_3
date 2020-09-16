#Actividad 3 - Sabores de Helado - Luis Enrique Preciado Muñiz

sabores=["Chocolate","Vainilla","Fresa","Pistache","Napolitano"]
nombre=input("Ingresa tu nombre: ")
apell=input("Ingresa tu apellido: ")
for i in range(5):
    print(f"{i+1}.-{sabores[i]}")
sabor=int(input("Ingresa el n° de sabor de helado que más te guste: "))
print(f"{nombre} {apell} el helado que mas te gusta es el de {sabores[sabor-1]}")
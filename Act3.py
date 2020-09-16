#Actividad 3 - Sabores de Helado - Luis Enrique Preciado Muñiz

sabores=["Chocolate","Vainilla","Fresa","Pistache","Napolitano"]
gusto=[]
nombre=input("Ingresa tu nombre: ")
apell=input("Ingresa tu apellido: ")
print("Del 1 al 10 indica que tanto te gusta cada sabor")
for i in range(5):
    gusto.append(int(input(f"{sabores[i]}: ")))
print(f"{nombre} {apell} los sabores que más te gustan ordenados de mayor a menor son: ")
for i in range(5):
    for j in range(i+1,5):
        if gusto[i]<gusto[j]:
            x=sabores[i]
            y=gusto[i]
            sabores[i]=sabores[j]
            gusto[i]=gusto[j]
            sabores[j]=x
            gusto[j]=y
for i in range(5):
    print(f"{i+1}.- {sabores[i]}")

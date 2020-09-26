def ingresar_dat(sab):
    gus = []
    print("Del 1 al 10 indica que tanto te gusta cada sabor")
    for i in range(5):
        gus.append(int(input(f"{sab[i]}: ")))
    return gus

def ordenar_dat(nom, ape, gus, sab):
    print(f"{nom} {ape} los sab que más te gustan ordenados de mayor a menor son: ")
    for i in range(5):
        for j in range(i+1,5):
            if gus[i]<gus[j]:
                x=sab[i]
                y=gus[i]
                sab[i]=sab[j]
                gus[i]=gus[j]
                sab[j]=x
                gus[j]=y
    return sab

def mostrar_dat(sab):
    for i in range(5):
        print(f"{i+1}.- {sab[i]}")
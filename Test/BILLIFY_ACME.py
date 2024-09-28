from Interfaz.Menu import Menu2
from Modelo.modelo import imp_fac

def imprimirMat(m):
    for f in range(len(m)):
        for c in range(len(m[f])):
            print(m[f][c], end = "\t")
        print("")

fd = open("Test/clientes.txt", "r")
clientes = []

for linea in fd:
    
    clientes.append(linea.split(";"))
imprimirMat(clientes)



fd = open("Test/productos.txt", "r")
productos = []

for linea in fd:
    
    productos.append(linea.split(";"))
imprimirMat(productos)



fd = open("Test/ventas.txt", "r")
ventas = []

for linea in fd:
    
    ventas.append(linea.split(";"))
imprimirMat(ventas)



print(">>> BILLIY_ACME <<<".center(60))

while True:
    op = Menu2()
    match op:
        case 1:
            imp_fac(ventas)
        case 2:
            print("")
        case 3:
            print("")
        case 4:
            print("")
        case 5:
            print("\n\nGracias por usar el software.\n".center(40))
            break



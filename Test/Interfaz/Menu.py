def Menu2():
    while True:
        
        print("")
        print(">>> Informe de ventas <<<".center(50))
        print("*" * 60)
        print("1. Copia Factura")
        print("2. Resumen de Facturas en un mes especifico")
        print("3. Diagrama comparativo")
        print("4. Productos comunes entre dos clientes")
        print("5. Salir")
        print("*" * 60)

        print("Opcion? >>> ", end="")
        try:
            opcion = int(input())
            if opcion < 1 or opcion > 5:
                print("ERROR. Opción NO válida")
                input("Presione cualquier tecla para volver al menu...")
            return opcion
            
        except ValueError:
            print("ERROR. Opción NO válida")
            input("Presione cualquier tecla para volver al menu...")
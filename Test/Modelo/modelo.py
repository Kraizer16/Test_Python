def imp_fac(mat):
    lstPrueba = []
    cod = input("Ingrese el codigo de la factura")
    for c in range(len(mat)):
        for f in range(len(mat[c])):
            loka = mat[f][c]
            lstPrueba.append(loka)
    print(lstPrueba)
    if cod in lstPrueba:
        print(cod)
    else:
        print("no esta")
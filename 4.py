def contar_positivos(lista):
    contador = 0

    for num in lista:
        if num > 0:
            contador += 1

    return contador


# ejemplo
datos = [-3, 5, 0, 7, -1, 2]
resultado = contar_positivos(datos)

print("Cantidad de números positivos:", resultado)
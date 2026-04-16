def primero_ultimo(lista):
    # validar que tenga al menos 2 elementos
    if len(lista) < 2:
        print("La lista debe tener al menos dos elementos")
        return None

    # devolver tupla con primero y último
    return (lista[0], lista[-1])


# ejemplo
datos = [10, 20, 30, 40]
resultado = primero_ultimo(datos)

if resultado != None:
    print("Resultado:", resultado)


# prueba con lista inválida
datos2 = [5]
resultado2 = primero_ultimo(datos2)
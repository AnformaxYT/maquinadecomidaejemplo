saldo = 5.0
cantidad_productos = 0

while True:
    print("\n========================")
    print("   MÁQUINA DE SNACKS")
    print("========================")
    print(f"Saldo disponible: Bs. {saldo:.2f}")
    print("\nProductos:")
    print("1. Papas:      Bs. 1.50")
    print("2. Chocolate:  Bs. 2.00")
    print("3. Refresco:   Bs. 2.50")
    print("4. Terminar compra")

    opcion = int(input("\nSeleccione una opción: "))

    if opcion == 1:
        precio = 1.50

        if saldo >= precio:
            saldo -= precio
            cantidad_productos += 1
            print("Producto comprado.")
        else:
            print("Plata insuficiente.")

    elif opcion == 2:
        precio = 2.00

        if saldo >= precio:
            saldo -= precio
            cantidad_productos += 1
            print("Producto comprado.")
        else:
            print("Plata insuficiente.")

    elif opcion == 3:
        precio = 2.50

        if saldo >= precio:
            saldo -= precio
            cantidad_productos += 1
            print("Producto comprado.")
        else:
            print("Plata insuficiente.")

    elif opcion == 4:
        break

    else:
        print("Opción inválida.")

print("\n========================")
print("RESUMEN DE COMPRA")
print("========================")
print("Productos comprados:", cantidad_productos)
print(f"Saldo restante: Bs. {saldo:.2f}")
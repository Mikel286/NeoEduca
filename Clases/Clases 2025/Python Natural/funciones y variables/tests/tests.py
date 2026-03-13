import main

def test_1():

    # Verificar que la función exista
    if not hasattr(main, "suma_enteros"):
        print("❌ No existe la función 'suma_enteros'")
        return

    tests = [
        (2, 3, 5),
        (11, 23, 34),
        (101, -34, 67)]

    for a, b, esperado in tests:
        try:
            result = main.suma_enteros(a, b)

            if not isinstance(result, int):
                print(f"❌ El resultado de {a} + {b} no es un entero")
                continue

            if result != esperado:
                print(f"❌ {a} + {b} = {result}, se esperaba {esperado}")
            else:
                print(f"✅ {a} + {b} = {result} correcto")

        except TypeError:
            print("❌ Error: revisa los parámetros de la función")
        except Exception:
            print("❌ Error interno al ejecutar la función")

def test_2():

    if not hasattr(main, "resta_enteros"):
        print("❌ No existe la función 'resta_enteros'")
        return

    tests = [
        (2, 3, -1),
        (11, 23, -12),
        (101, -34, 135)]

    for a, b, esperado in tests:
        try:
            result = main.resta_enteros(a, b)

            if not isinstance(result, int):
                print(f"❌ El resultado de {a} - {b} no es un entero")
                continue

            if result != esperado:
                print(f"❌ {a} - {b} = {result}, se esperaba {esperado}")
            else:
                print(f"✅ {a} - {b} = {result} correcto")

        except TypeError:
            print("❌ Error: revisa los parámetros de la función")
        except Exception:
            print("❌ Error interno al ejecutar la función")

def test_3():

    if not hasattr(main, "multiplicacion_enteros"):
        print("❌ No existe la función 'multiplicacion_enteros'")
        return

    tests = [
        (2, 3, 6),
        (11, 23, 253),
        (101, -34, -3434)]

    for a, b, esperado in tests:
        try:
            result = main.multiplicacion_enteros(a, b)

            if not isinstance(result, int):
                print(f"❌ El resultado de {a} * {b} no es un entero")
                continue

            if result != esperado:
                print(f"❌ {a} * {b} = {result}, se esperaba {esperado}")
            else:
                print(f"✅ {a} * {b} = {result} correcto")

        except TypeError:
            print("❌ Error: revisa los parámetros de la función")
        except Exception:
            print("❌ Error interno al ejecutar la función")

def test_4():

    if not hasattr(main, "division_enteros"):
        print("❌ No existe la función 'division_enteros'")
        return

    tests = [
        (2, 3, 0),
        (11, 23, 0),
        (101, -34, -2)]

    for a, b, esperado in tests:
        try:
            result = main.division_enteros(a, b)

            if not isinstance(result, int):
                print(f"❌ El resultado de {a} / {b} = {result} no es un entero")
                continue

            if result != esperado:
                print(f"❌ {a} / {b} = {result}, se esperaba {esperado}")
            else:
                print(f"✅ {a} / {b} = {result} correcto")

        except TypeError:
            print("❌ Error: revisa los parámetros de la función")
        except Exception:
            print("❌ Error interno al ejecutar la función")

if __name__ == "__main__":

    test_4()            

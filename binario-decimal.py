def convertir_a_decimal(binario):
    res = 0
    for i in range(len(str(binario))):
        mult = int(binario[i]) * (2**i)
        res = res + mult
    return res


def convertir_a_binario(decimal):
    binario = ""
    while decimal // 2 != 0:
        binario = str(decimal % 2) + binario
        decimal = decimal // 2
    return str(decimal) + binario


def imprimir_resultado(resultado):
    print("El valor de {} es {}".format(valor, resultado))


opcion = int(input(
    "1-> Para convertir de DECIMAL a BINARIO. \n2-> Para convertir de BINARIO a DECIMAL.\n¿Qué conversión deseas hacer? "))

if opcion == 1:
    valor = int(input("\nIngresa el decimal: "))
    conversion = convertir_a_binario(valor)
    imprimir_resultado(conversion)
elif opcion == 2:
    valor = input("\nIngresa el binario: ")
    conversion = convertir_a_decimal(valor)
    imprimir_resultado(conversion)
else:
    print("\n{} no es una opción.".format(opcion))

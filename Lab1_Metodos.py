def binario_a_decimal(binario):
    if binario[0] == '1':
        return -((1 << (len(binario)-1)) - int(binario[1:], 2))
    else:
        return int(binario[1:], 2)

def decimal_a_binario(decimal):
    if decimal >= 0:
        return '0' + format(decimal, '015b')
    else:
        return '1' + format((1 << 15) + decimal, '014b')  

def mostrar_numero(numero, tipo):
    signo = numero[0]
    mantisa = numero[1:]
    if tipo == 'binario':
        print(f"Signo: {signo}")
        print(f"Mantisa: {mantisa}")
        print(f"Valor decimal: {binario_a_decimal(numero)}")
    elif tipo == 'decimal':
        print(f"Signo: {'+' if int(signo) == 0 else '-'}")
        print(f"Valor binario: {numero}")
        print(f"Signo: {signo}")
        print(f"Mantisa: {mantisa}")

def calculo():
    num = input("Ingrese un número con su respectivo sufijo b (si es binario) o d (si es decimal): ")
    if num.endswith('b'):
        binario = num[:-1]
        mostrar_numero(binario, 'binario')
    elif num.endswith('d'):
        decimal = int(num[:-1])
        mostrar_numero(decimal_a_binario(decimal), 'decimal')
    else:
        print("Notación no identificada, por favor vuelva a intentarlo")

calculo()

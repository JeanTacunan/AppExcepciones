def leer_numero_natural():
    while True:
        try:

            entrada = input("Ingrese un número natural: ")

            numero = int(entrada)

            if numero <= 0:
                raise ValueError("El número debe ser un entero positivo mayor que 0.")

            return numero
        except ValueError as e:

            print(f"Error: {e}. Intente nuevamente.")

def calcular_divisores(numero):

    divisores = []

    for i in range(1, numero + 1):
        if numero % i == 0:
            divisores.append(i)

    return divisores


if __name__ == '__main__':

    numero = leer_numero_natural()

    divisores = calcular_divisores(numero)

    print(f"Los divisores de {numero} son: {divisores}")
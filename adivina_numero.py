import random     ##Este módulo implementa generadores de números pseudoaleatorios para varias distribuciones


def run():
    numero_aleatorio = random.randint(1, 100)       ##defino un rango de acción  La función randint() devuelve un número entero incluido entre los valores indicados.
    numero_usuario = int(input('Ingrese su número, del 1 al 100:\n')) ##numero que ingresará el usuario, lo convierto a entero, a su vez \n el numero a ingresar se va al renglon siguiente
    while numero_usuario != numero_aleatorio:        ##con while se prueba si se encontro o no el numero
        if numero_usuario < numero_aleatorio:
            print('Elige un número mayor')              ##con if se compara el numero aleatorio y el del usuario
        else:
            print('Elige un número menor')
        numero_usuario = int(input('ingrese un nuevo número:\n')) ##no encontraso el numero se pide que reingrese 
    print('¡GANASTE!')        ##una vez que aciertes se imprime que ganaste


if __name__ == '__main__':
    run()
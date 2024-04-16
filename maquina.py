#Lixander Ysael Hilario Lopez 2021-1855

import sys


class Vaso:
    def __init__(self, cantidad_vasos):
        self.cantidad_vasos = cantidad_vasos

    def has_vasos(self):
        return self.cantidad_vasos > 0

    def give_vasos(self):
        if self.has_vasos():
            self.cantidad_vasos -= 1
            return True
        else:
            print("No hay suficientes vasos.")
            return False

class Cafetera:
    def __init__(self, cantidad_cafe):
        self.cantidad_cafe = cantidad_cafe

    def has_cafe(self, cantidad_cafe):
        return self.cantidad_cafe >= cantidad_cafe

    def give_cafe(self, cantidad_cafe):
        if self.has_cafe(cantidad_cafe):
            self.cantidad_cafe -= cantidad_cafe
            return True
        else:
            print("No hay suficiente café.")
            return False

class Azucarero:
    def __init__(self, cantidad_azucar):
        self.cantidad_azucar = cantidad_azucar

    def has_azucar(self, cantidad_azucar):
        return self.cantidad_azucar >= cantidad_azucar

    def give_azucar(self, cantidad_azucar):
        if self.has_azucar(cantidad_azucar):
            self.cantidad_azucar -= cantidad_azucar
            return True
        else:
            print("No hay suficiente azúcar.")
            return False

class MaquinaDeCafe:
    def __init__(self):
        self.vasos_pequenos = Vaso(10)
        self.vasos_medianos = Vaso(10)
        self.vasos_grandes = Vaso(10)
        self.cafetera = Cafetera(100)
        self.azucarero = Azucarero(50)

    def servir_cafe(self, tamano, cantidad_azucar):
        if tamano == 'pequeno' and self.vasos_pequenos.give_vasos():
            cantidad_cafe = 3
        elif tamano == 'mediano' and self.vasos_medianos.give_vasos():
            cantidad_cafe = 5
        elif tamano == 'grande' and self.vasos_grandes.give_vasos():
            cantidad_cafe = 7
        else:
            print("Opción de tamaño no válida o no hay vasos disponibles.")
            return

        if self.cafetera.give_cafe(cantidad_cafe) and self.azucarero.give_azucar(cantidad_azucar):
            print(f"Disfruta tu café {tamano} con {cantidad_azucar} cucharada(s) de azúcar!")
        else:
            print("No se pudo servir el café.")

# Programa principal
maquina = MaquinaDeCafe()

def main():
    while True:
        print("\nBienvenido a la máquina de café.")
        print("1. Vaso pequeño - 3 Oz de café")
        print("2. Vaso mediano - 5 Oz de café")
        print("3. Vaso grande - 7 Oz de café")
        print("4. Salir")
        opcion = input("Elige el tamaño del café (1, 2, 3) o presiona '4' para salir: ")

        if opcion == '4':
            print("Gracias por visitar la máquina de café. Esto fue hecho por Lixander Hilario. ¡Adiós!")
            break

        cantidad_azucar = int(input("¿Cuántas cucharadas de azúcar deseas?: "))
        
        tamanos = {'1': 'pequeno', '2': 'mediano', '3': 'grande'}
        tamano_cafe = tamanos.get(opcion, None)

        if tamano_cafe:
            maquina.servir_cafe(tamano_cafe, cantidad_azucar)
        else:
            print("Opción no válida. Intente de nuevo.")

if __name__ == '__main__':
    main()
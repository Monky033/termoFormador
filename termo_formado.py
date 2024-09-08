class MaquinaTermoformado:
    def __init__(self, temperatura_ambiente=20, temperatura_optima=150, material_disponible=1000):
        self.__temperatura_actual = temperatura_ambiente
        self.__temperatura_optima = temperatura_optima
        self.__material_disponible = material_disponible



    def __get_temperatura_actual(self):
        return self.__temperatura_actual

    def __get_temperatura_optima(self):
        return self.__temperatura_optima

    def __get_material_disponible(self):
        return self.__material_disponible



    def __set_temperatura_actual(self, nueva_temperatura):
        if 20 <= nueva_temperatura <= self.__temperatura_optima:
            self.__temperatura_actual = nueva_temperatura
        else:
            print("Error: La temperatura no puede ser inferior a la temperatura ambiente ni superior a la temperatura óptima.")

    def __set_temperatura_optima(self, nueva_temperatura_optima):
        if nueva_temperatura_optima > self.__temperatura_actual:
            self.__temperatura_optima = nueva_temperatura_optima
        else:
            print("Error: La temperatura óptima debe ser mayor a la temperatura actual.")

    def __set_material_disponible(self, nuevo_material):
        if nuevo_material >= 0:
            self.__material_disponible = nuevo_material
        else:
            print("Error: La cantidad de material no puede ser negativa.")



    def calentar(self):
        if self.__temperatura_actual < self.__temperatura_optima:
            self.__temperatura_actual += 5
            print(f"Calentando... Temperatura actual: {self.__temperatura_actual}°C")
        else:
            print("La temperatura ya es óptima para el termoformado.")

    def formar(self, tamaño_lote):
        if self.__temperatura_actual >= self.__temperatura_optima:
            if self.__material_disponible >= tamaño_lote:
                self.__material_disponible -= tamaño_lote
                print(f"Formando lote de tamaño {tamaño_lote}... Material restante: {self.__material_disponible} unidades.")
            else:
                print("No hay suficiente material para formar este lote.")
        else:
            print("La temperatura no es suficiente para realizar el termoformado.")

    def enfriar(self):
        if self.__temperatura_actual > 20:
            self.__temperatura_actual -= 10
            print(f"Enfriando... Temperatura actual: {self.__temperatura_actual}°C")
        else:
            print("La máquina ya está a temperatura ambiente.")



    def __str__(self):
        return (f"Maquina de Termoformado:\n"
                f"Temperatura Actual: {self.__temperatura_actual}°C\n"
                f"Material Disponible: {self.__material_disponible} unidades\n"
                f"Temperatura Óptima: {self.__temperatura_optima}°C")


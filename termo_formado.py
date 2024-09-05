class MaquinaTermoformado:
    def __init__(self, temperatura_ambiente=20, temperatura_optima=150, material_disponible=1000):
        self._temperatura_actual = temperatura_ambiente
        self._temperatura_optima = temperatura_optima
        self._material_disponible = material_disponible



    def get_temperatura_actual(self):
        return self._temperatura_actual

    def get_temperatura_optima(self):
        return self._temperatura_optima

    def get_material_disponible(self):
        return self._material_disponible



    def set_temperatura_actual(self, nueva_temperatura):
        if 20 <= nueva_temperatura <= self._temperatura_optima:
            self._temperatura_actual = nueva_temperatura
        else:
            print("Error: La temperatura no puede ser inferior a la temperatura ambiente ni superior a la temperatura óptima.")

    def set_temperatura_optima(self, nueva_temperatura_optima):
        if nueva_temperatura_optima > self._temperatura_actual:
            self._temperatura_optima = nueva_temperatura_optima
        else:
            print("Error: La temperatura óptima debe ser mayor a la temperatura actual.")

    def set_material_disponible(self, nuevo_material):
        if nuevo_material >= 0:
            self._material_disponible = nuevo_material
        else:
            print("Error: La cantidad de material no puede ser negativa.")




    def calentar(self):
        if self._temperatura_actual < self._temperatura_optima:
            self._temperatura_actual += 5
            print(f"Calentando... Temperatura actual: {self._temperatura_actual}°C")
        else:
            print("La temperatura ya es óptima para el termoformado.")

    def formar(self, tamaño_lote):
        if self._temperatura_actual >= self._temperatura_optima:
            if self._material_disponible >= tamaño_lote:
                self._material_disponible -= tamaño_lote
                print(f"Formando lote de tamaño {tamaño_lote}... Material restante: {self._material_disponible} unidades.")
            else:
                print("No hay suficiente material para formar este lote.")
        else:
            print("La temperatura no es suficiente para realizar el termoformado.")

    def enfriar(self):
        if self._temperatura_actual > 20:
            self._temperatura_actual -= 10
            print(f"Enfriando... Temperatura actual: {self._temperatura_actual}°C")
        else:
            print("La máquina ya está a temperatura ambiente.")

    def __str__(self):
        return (f"Maquina de Termoformado:\n"
                f"Temperatura Actual: {self._temperatura_actual}°C\n"
                f"Material Disponible: {self._material_disponible} unidades\n"
                f"Temperatura Óptima: {self._temperatura_optima}°C")

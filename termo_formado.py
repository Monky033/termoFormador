class MaquinaTermoformado:
    def __init__(self, temperatura_ambiente=20, temperatura_optima=150, material_disponible=1000):
        self.temperatura_actual = temperatura_ambiente
        self.temperatura_optima = temperatura_optima
        self.material_disponible = material_disponible

    def calentar(self):
        if self.temperatura_actual < self.temperatura_optima:
            self.temperatura_actual += 5
            print(f"Calentando... Temperatura actual: {self.temperatura_actual}°C")
        else:
            print("La temperatura ya es óptima para el termoformado.")

    def formar(self, tamaño_lote):
        if self.temperatura_actual >= self.temperatura_optima:
            if self.material_disponible >= tamaño_lote:
                self.material_disponible -= tamaño_lote
                print(f"Formando lote de tamaño {tamaño_lote}... Material restante: {self.material_disponible} unidades.")
            else:
                print("No hay suficiente material para formar este lote.")
        else:
            print("La temperatura no es suficiente para realizar el termoformado.")

    def enfriar(self):
        if self.temperatura_actual > 20:
            self.temperatura_actual -= 10
            print(f"Enfriando... Temperatura actual: {self.temperatura_actual}°C")
        else:
            print("La máquina ya está a temperatura ambiente.")

    def __str__(self):
        return (f"Maquina de Termoformado:\n"
                f"Temperatura Actual: {self.temperatura_actual}°C\n"
                f"Material Disponible: {self.material_disponible} unidades\n"
                f"Temperatura Óptima: {self.temperatura_optima}°C")


maquina = MaquinaTermoformado()


for _ in range(30):  
    maquina.calentar()


maquina.formar(300)


for _ in range(15):  
    maquina.enfriar()


print(maquina)

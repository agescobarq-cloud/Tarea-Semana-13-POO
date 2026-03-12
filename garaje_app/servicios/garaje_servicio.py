from modelos.vehiculo import Vehiculo


class GarajeServicio:
    def __init__(self):
        self.vehiculos: list[Vehiculo] = []

    def agregar_vehiculo(self, placa: str, marca: str, propietario: str) -> tuple[bool, str]:
        placa = placa.strip().upper()
        
        # Validaciones básicas
        if not placa:
            return False, "La placa es obligatoria"
        if not marca:
            return False, "La marca es obligatoria"
        if not propietario:
            return False, "El propietario es obligatorio"

        # Verificar que no exista ya esa placa
        if any(v.placa == placa for v in self.vehiculos):
            return False, f"El vehículo con placa {placa} ya está registrado"

        vehiculo = Vehiculo(placa, marca, propietario)
        self.vehiculos.append(vehiculo)
        return True, "Vehículo agregado correctamente"

    def obtener_todos(self) -> list[Vehiculo]:
        return self.vehiculos.copy()

    def limpiar(self):
        self.vehiculos.clear()
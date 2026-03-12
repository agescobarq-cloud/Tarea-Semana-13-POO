class Vehiculo:
    def __init__(self, placa: str, marca: str, propietario: str):
        self.placa = placa.strip().upper()
        self.marca = marca.strip().title()
        self.propietario = propietario.strip().title()

    def __str__(self):
        return f"{self.placa} | {self.marca} | {self.propietario}"

    def to_dict(self):
        return {
            "placa": self.placa,
            "marca": self.marca,
            "propietario": self.propietario
        }

    @classmethod
    def from_dict(cls, data: dict):
        return cls(
            data["placa"],
            data["marca"],
            data["propietario"]
        )
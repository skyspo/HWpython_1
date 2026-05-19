class Mailing:
    def __init__(self, to_address, from_address, cost, track):
        self.to_adr = to_address
        self.from_adr = from_address
        self.cost = cost
        self.track = track

    def __str__(self):
        return (f"Отправление {self.track} из {self.from_adr.index}, "
                f"{self.from_adr.city}, {self.from_adr.street}"
                f"{self.from_adr.dom}, {self.from_adr.kv}"
                f" в {self.to_adr.city}, {self.to_adr.street}"
                f"{self.to_adr.dom}, {self.to_adr.kv}"
                f" Стоимость {self.cost} рублей"
                )
               




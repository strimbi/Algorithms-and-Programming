from dataclasses import dataclass


@dataclass(order=True)
class Numarinchirieri:
    id_client: int
    numar_carti: int
    nume: str

    def __str__(self):
        return "Client: " + str(self.id_client) + " || Nume: " + str(self.nume) + \
               " || Numar carti: " + str(self.numar_carti)

from dataclasses import dataclass


@dataclass
class Client:
    id: int
    nume: str
    cnp: str

    def __str__(self):
        return "Client " + str(self.id) + " || Nume: " + str(self.nume) + " / Cnp: " + str(self.cnp)

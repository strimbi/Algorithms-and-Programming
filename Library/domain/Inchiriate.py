from dataclasses import dataclass


@dataclass
class Inchiriate:
    id_client: int
    id_carte: int

    def __str__(self):
        return "Client: " + str(self.id_client) + " || Carte: " + str(self.id_carte)

from dataclasses import dataclass


@dataclass(order=True)
class Book:
    id: int
    titlu: str
    descriere: str
    autor: str

    def __str__(self):
        return "Carte " + str(self.id) + " || Titlu: " + str(self.titlu) + " / Descriere: " + \
               str(self.descriere) + " / Autor: " + str(self.autor)

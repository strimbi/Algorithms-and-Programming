from dataclasses import dataclass


@dataclass
class Coffee:
    """
    Creez o clasa tip dataclass cu id, nume, tara de origine si pret pt o cafea
    """
    id: int  # unique!
    name: str
    country: str
    price: float

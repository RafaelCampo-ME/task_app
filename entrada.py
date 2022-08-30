import random 
import string
from dataclasses import dataclass

##Voy a construir una clase de registro que guarde un registro contable


def generate_id() -> str:
    return ''.join(random.choices(string.ascii_uppercase, k=12))

@dataclass(frozen=False)
class Person:
    name: str
    adress: str
    active: bool = True  ##Valor de default



    def __str__(self) -> str:
        return f"{self.name},{self.address}"

generate_id()


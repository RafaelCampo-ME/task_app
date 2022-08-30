import random
from sqlite3 import Timestamp 
import string
from dataclasses import dataclass, field

##Voy a construir una clase de registro que guarde un registro contable


def generate_id() -> str:
    print("Id generado")
    return ''.join(random.choices(string.ascii_uppercase, k=12))

@dataclass(frozen=False)
class AccountingEntry:
    entry_id: str = field(default_factory=generate_id())
    date_created: str
    merchant: str
    entry_descrip: str
    entry_amount: str
    entry_class: str = "Gastos"
    meta_data: list[str] = field(default_factory=list)  ##Funcion


###Meterle suave de validacion para los campos entry_amount y merchant 

 
 

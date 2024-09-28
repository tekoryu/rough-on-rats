from pydantic import BaseModel
from typing import Optional, List
import json
import numpy as np


class PassageiroViewSchema(BaseModel):
    """Define como um Passageiro será retornado
    """
    name: str = "Maria"
    pclass: int = 3
    sex: str = "male"
    age: int = 72
    sibsp: int = 2
    parch: int = 2
    fixed_fare: int = 250.0
    pronome: int = 1
    survived: int = 0


class PassageiroBuscaSchema(BaseModel):
    """Define como deve ser a estrutura que representa a busca.
    Ela será feita com base no nome do Passageiro.
    """
    name: str = "Maria"


class PassageiroSchema(BaseModel):
    """ Determina o grau de aproxin
    """
    name: str = "Maria"
    pclass: int = 6
    sex: str = "male"
    age: int = 72
    sibsp: int = 2
    parch: int = 2
    fare: int = 250.0
    pronome: int = 1
from datetime import datetime
from typing import Any, Dict
import json

class Horodatable:
    def horodatage(self):
        print(f"[LOG] Action à {datetime.now()}")

class Validable:
    def valider(self):
        if not getattr(self, "titre", None):
            raise ValueError("Titre manquant")
        if not getattr(self, "contenu", None):
            raise ValueError("Contenu manquant")
        print("Validation OK")

class Serializable:
    def to_json(self) -> str:
        instance_data: Dict[str, Any] = self.__dict__
        return json.dumps(instance_data, ensure_ascii=False)

class Document(Horodatable, Validable, Serializable):
    def __init__(self, titre, contenu):
        self.titre = titre
        self.contenu = contenu

    def sauvegarder(self):
        self.horodatage()
        self.valider()
        print(f"Document '{self.titre}' sauvegardé.")
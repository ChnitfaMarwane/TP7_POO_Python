import json
from datetime import datetime
from typing import Any, Dict

class Serializable:
    def to_json(self) -> str:
        # __dict__ renvoie les attributs d'instance
        instance_data: Dict[str, Any] = self.__dict__.copy()
        
        # Supprimer les attributs internes des mixins pour un JSON plus propre
        if 'historique' in instance_data:
            del instance_data['historique']
            
        return json.dumps(instance_data, ensure_ascii=False)

    @classmethod
    def from_json(cls, json_str):
        # Utilisation de **kwargs pour appeler le constructeur avec les données du JSON
        return cls(**json.loads(json_str))

class Historisable:
    # Utilisation d'un constructeur non trivial
    def __init__(self, *args, **kwargs):
        self.historique = []
        # Appeler le constructeur de la classe parente suivante dans la MRO
        super().__init__(*args, **kwargs)

    def enregistrer_etat(self):
        # Utiliser un dictionnaire de copie pour éviter les références
        self.historique.append((datetime.now().isoformat(), self.__dict__.copy()))

class Journalisable:
    def journaliser(self, message):
        print(f"[Journal] {datetime.now().isoformat(timespec='milliseconds')}: {message}")

class Contrat(Historisable, Serializable, Journalisable):
    # L'ordre d'héritage est important pour la MRO (Historisable doit s'initialiser en premier)
    def __init__(self, id_contrat, description):
        # Appelle le __init__ de Historisable, qui appellera ensuite le __init__ de object
        super().__init__() 
        self.id = id_contrat
        self.description = description
        
        # Enregistrer l'état initial
        self.enregistrer_etat()

    def modifier(self, nouvelle_desc):
        self.journaliser(f"Modification du contrat {self.id}")
        self.enregistrer_etat() # Enregistre l'état actuel avant modification
        self.description = nouvelle_desc
from datetime import datetime
from typing import List, Dict, Any
import copy

class ValidationMixin:
    def valider(self):
        # Vérifie que le titre est présent et non vide
        if not getattr(self, 'titre', '').strip():
            raise ValueError("Le titre de la tâche est obligatoire.")

class HistoriqueMixin:
    def __init__(self, *args, **kwargs):
        # Liste pour stocker l'historique des descriptions
        self._historique_descriptions: List[Dict[str, Any]] = []
        # Appel du constructeur de la classe parente suivante
        super().__init__(*args, **kwargs)

    def _enregistrer_historique(self):
        if hasattr(self, 'description'):
            # Enregistre une copie de l'état actuel de la description avec un horodatage
            self._historique_descriptions.append({
                "date": datetime.now().isoformat(timespec='seconds'),
                "description": copy.deepcopy(self.description)
            })

    def afficher_historique(self):
        print(f"\n--- Historique de la tâche '{self.titre}' ---")
        if not self._historique_descriptions:
            print("Aucune modification enregistrée.")
            return

        for version in self._historique_descriptions:
            print(f"[{version['date']}] : {version['description']}")

class JournalisationMixin:
    def journaliser(self, action: str):
        date_heure = datetime.now().isoformat(timespec='seconds')
        titre = getattr(self, 'titre', '[Tâche Sans Titre]')
        print(f"[JOURNAL {date_heure}] Tâche '{titre}': {action}")

# La classe métier Tâche hérite des Mixins
# L'ordre MRO est important : HistoriqueMixin doit être appelé en premier par super()
class Tache(ValidationMixin, HistoriqueMixin, JournalisationMixin):
    def __init__(self, titre: str, description: str):
        # Initialisation du mixin Historique qui appellera super() -> object.__init__
        super().__init__() 
        
        # Définition des attributs avant la validation et l'enregistrement
        self.titre = titre
        self.description = description
        self.date_creation = datetime.now().isoformat(timespec='seconds')

        # Validation initiale
        self.valider()
        self.journaliser(f"Création (Date: {self.date_creation})")
        self._enregistrer_historique()

    def mettre_a_jour(self, nouvelle_description: str):
        # 1. Enregistre la version actuelle AVANT modification
        self._enregistrer_historique()
        
        # 2. Met à jour la description
        self.description = nouvelle_description
        
        # 3. Journalise l'action
        self.journaliser("Mise à jour de la description.")
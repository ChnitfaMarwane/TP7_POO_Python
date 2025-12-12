from mixins_contrat import Contrat
import json

if __name__ == '__main__':
    c = Contrat(1, "flan fartlan contrat initial")
    print(f"ID: {c.id}, Desc: {c.description}")
    
    print("\n--- Modification ---")
    c.modifier("flan fartlan contrat révisé")
    print(f"Nouvelle description: {c.description}")
    
    print("\n--- Sérialisation JSON ---")
    json_output = c.to_json()
    print(json_output)
    
    print("\n--- Historique des états ---")
    for date_time, etat in c.historique:
        if 'historique' in etat:
            del etat['historique']
        print(f"[{date_time[:23]}] {etat}")

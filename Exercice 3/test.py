from mixins_tache import Tache

if __name__ == '__main__':
    # --- 1. Test nominal (Création et Mise à jour) ---
    print("--- 1. Test Nominal ---")
    tache_flan = Tache("Rapport Mensuel Flan", "Rédiger l'introduction.")
    print(f"Tâche actuelle : {tache_flan.description}")

    # Première mise à jour
    tache_flan.mettre_a_jour("Ajouter les données du T1.")
    print(f"Tâche actuelle après MAJ 1 : {tache_flan.description}")

    # Deuxième mise à jour
    tache_flan.mettre_a_jour("Finaliser et valider la mise en page.")
    print(f"Tâche actuelle après MAJ 2 : {tache_flan.description}")

    # Afficher l'historique complet
    tache_flan.afficher_historique()

    # --- 2. Test de validation (Titre vide) ---
    print("\n--- 2. Test de Validation (Titre vide) ---")
    try:
        Tache("", "Description valide.")
    except ValueError as e:
        print(f"Erreur traitée : {e}")
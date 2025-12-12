from mixins_document import Document, Horodatable, Validable, Serializable
import json

if __name__ == '__main__':
    doc = Document("Rapport flan", "Contenu important fartlan")

    doc.sauvegarder()

    json_output = doc.to_json()
    print(f"\nSérialisation : {json_output}")

    doc_err_titre = Document("", "Contenu présent")
    print("\nTest d'erreur : Titre manquant")
    try:
        doc_err_titre.sauvegarder()
    except ValueError as e:
        print(f"Erreur traitée : {e}")

    doc_err_contenu = Document("Rapport OK", "")
    print("\nTest d'erreur : Contenu manquant")
    try:
        doc_err_contenu.sauvegarder()
    except ValueError as e:
        print(f"Erreur traitée : {e}")

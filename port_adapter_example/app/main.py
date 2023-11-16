"""
Fichier principal de l'application
"""
import sys
from app.core.adapters.factory import get_parseur
from app.core.constants import ABAQUS_FILE_PATH, NASTRAN_FILE_PATH


def main():
    """Fonction principale"""

    choix = input("Choisissez le fichier (1: Abaqus, 2: Nastran): ")

    if choix == "1":
        file = ABAQUS_FILE_PATH
    elif choix == "2":
        file = NASTRAN_FILE_PATH
    else:
        print("Choix invalide")
        sys.exit()

    print(f"Chargement du fichier {str(file)}")
    print("Début du programme : \n")

    parseur = get_parseur(file)

    nodes = parseur.get_nodes()

    print(nodes, "\n")

    elements = parseur.get_elements()

    print(elements, "\n")

    print("Fin du programme")


if __name__ == "__main__":
    main()

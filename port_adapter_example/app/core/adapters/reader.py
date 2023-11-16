"""Module pour lire un fichier."""
from pathlib import Path


def read_file(file_path: Path | str):
    """Lire un fichier et retourner son contenu sous forme de liste de lignes."""
    with open(file_path, "r", encoding="utf-8") as f:
        lines = f.readlines()

    return lines

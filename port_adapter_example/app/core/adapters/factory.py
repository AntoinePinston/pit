"""Factory module for parseur."""
import os
from pathlib import Path

from app.core.adapters.abaqus_adapter import AbaqusParseur
from app.core.adapters.nastran_adapter import NastranParseur
from app.core.ports.modele import ModeleElementFini


def get_parseur(file_path: Path | str) -> ModeleElementFini:
    """Retourne un parseur en fonction de l'extension du fichier."""

    ext = os.path.splitext(file_path)[1]

    if ext == ".inp":
        return AbaqusParseur(file_path)
    elif ext == ".bdf":
        return NastranParseur(file_path)

    raise ValueError("Format de fichier non supporté")

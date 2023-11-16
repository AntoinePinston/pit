"""Teste le parseur Abaqus."""
from app.core.adapters.abaqus_adapter import AbaqusParseur
from app.core.constants import ABAQUS_FILE_PATH


def test_abaqus_parseur():
    """Teste le parseur Abzqus."""
    nastran_parseur = AbaqusParseur(ABAQUS_FILE_PATH)

    nodes = nastran_parseur.get_nodes()
    elements = nastran_parseur.get_elements()

    assert len(nodes) == 6
    assert len(elements) == 5

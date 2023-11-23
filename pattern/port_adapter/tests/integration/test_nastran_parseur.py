



from app.core.adapters.nastran_adapter import NastranParseur
from app.core.constants import NASTRAN_FILE_PATH


def test_nastran_parseur():
    """Teste le parseur Nastran."""
    nastran_parseur = NastranParseur(NASTRAN_FILE_PATH)

    nodes = nastran_parseur.get_nodes()
    elements = nastran_parseur.get_elements()

    assert len(nodes) == 6
    assert len(elements) == 5

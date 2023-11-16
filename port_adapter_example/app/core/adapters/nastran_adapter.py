""" Adaptateur pour le format Nastran """
from pathlib import Path
from typing import List

from app.core.adapters.reader import read_file
from app.core.ports.modele import Element, ModeleElementFini, Node, Poutre


def split_by_8(text: str, chunk_size: int = 8) -> List[str]:
    """Découpe une chaîne de caractères en plusieurs sous-chaînes (chunks) de taille définie."""
    text = text.replace("\n", "")
    return [text[i : i + chunk_size].strip() for i in range(0, len(text), chunk_size)]


class NastranNode(Node):
    """Noeud pour le format Nastran"""

    @classmethod
    def from_card(cls, card: str):
        """Retourne un noeud à partir d'une carte"""

        card = split_by_8(card)
        return cls(int(card[1]), float(card[3]), float(card[4]), float(card[5]))


class NastranPoutre(Poutre):
    """Poutre pour le format Nastran"""

    @classmethod
    def from_card(cls, card: str):
        """Retourne une poutre à partir d'une carte"""

        card = split_by_8(card)
        return cls(int(card[1]), [int(card[3]), int(card[4])])


class NastranParseur(ModeleElementFini):
    """Parseur pour le format Nastran"""

    def __init__(self, file_path: Path | str):
        self.lines = read_file(file_path)

    def get_nodes(self) -> dict[int, Node]:
        """Retourne noeuds du modèle"""

        node_cards = {}
        for line in self.lines:
            if line.startswith("GRID"):
                node = NastranNode.from_card(line)
                node_cards[node.n_id] = node

        return node_cards

    def get_elements(self) -> dict[int, Element]:
        """Retourne les elements du modèle"""

        element_cards = {}
        for line in self.lines:
            if line.startswith("CBEAM"):
                element = NastranPoutre.from_card(line)
                element_cards[element.e_id] = element

        return element_cards

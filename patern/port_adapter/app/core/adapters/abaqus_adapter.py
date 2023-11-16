""" Adaptateur pour le format Abaqus """
from pathlib import Path
from typing import List
from app.core.adapters.reader import read_file

from app.core.ports.modele import Element, ModeleElementFini, Node, Poutre


def abaqus_split(text: str) -> List[str]:
    """Découpe une chaîne de caractères en plusieurs sous-chaînes (chunks) de taille définie."""
    text = text.replace("\n", "").strip()
    return [element.strip() for element in text.split(",")]


class AbaqusNode(Node):
    """Noeud pour le format Nastran"""

    @classmethod
    def from_card(cls, card: str):
        """Retourne un noeud à partir d'une carte"""

        card = abaqus_split(card)
        return cls(int(card[0]), float(card[1]), float(card[2]), float(card[3]))


class AbaqusPoutre(Poutre):
    """Poutre pour le format Nastran"""

    @classmethod
    def from_card(cls, card: str):
        """Retourne une poutre à partir d'une carte"""

        card = abaqus_split(card)
        return cls(int(card[0]), [int(card[1]), int(card[2])])


class AbaqusParseur(ModeleElementFini):
    """Parseur pour le format Nastran"""

    def __init__(self, file_path: Path | str):
        self.lines = read_file(file_path)

    def get_nodes(self) -> dict[int, Node]:
        """Retourne noeuds du modèle"""

        node_cards = {}

        start_condition = "*Node"
        end_condition = "\n"

        for line in self.lines:
            if line.startswith(start_condition):
                start_index = self.lines.index(line) + 1
                end_index = self.lines.index(end_condition, start_index)

        for node in self.lines[start_index:end_index]:
            node = AbaqusNode.from_card(node)
            node_cards[node.n_id] = node

        return node_cards

    def get_elements(self) -> dict[int, Element]:
        """Retourne les elements du modèle"""

        element_cards = {}

        start_condition = "*Element"
        is_start = False
        end_condition = "\n"
        end_index = len(self.lines)

        for line in self.lines:
            if line.startswith(start_condition):
                start_index = self.lines.index(line) + 1
                is_start = True
            if is_start and line.startswith(end_condition):
                end_index = self.lines.index(line)

        for element in self.lines[start_index:end_index]:
            element = AbaqusPoutre.from_card(element)
            element_cards[element.e_id] = element

        return element_cards

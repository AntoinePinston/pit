"""Module pour les modèles d'éléments finis"""
from abc import ABC, abstractmethod


class Node(ABC):
    """Classe pour les noeuds"""

    def __init__(self, n_id: int, x: float, y: float, z: float):
        self.n_id = n_id
        self.x = x
        self.y = y
        self.z = z

    @classmethod
    def from_card(cls, card: str):
        """Retourne un noeud à partir d'une carte"""
        raise NotImplementedError

    def __repr__(self) -> str:
        return f"Node({self.n_id}, {self.x}, {self.y}, {self.z})"


class Element(ABC):
    """Classe pour les éléments"""

    def __init__(self, e_id: int, nodes: list[int]):
        self.e_id = e_id
        self.nodes = nodes

    @classmethod
    def from_card(cls, card: str):
        """Retourne un noeud à partir d'une carte"""
        raise NotImplementedError

    def __repr__(self) -> str:
        return f"Element({self.e_id}, {self.nodes})"


class Poutre(Element):
    """Classe pour les poutres"""

    def __init__(self, e_id: int, nodes: list[int]):
        """Initialise une poutre, vérifie qu'elle a 2 noeuds"""
        super().__init__(e_id, nodes)
        if len(nodes) != 2:
            raise ValueError("Une poutre doit avoir 2 noeuds")


class ModeleElementFini(ABC):
    """Classe abstraite pour les modèles d'éléments finis"""

    @abstractmethod
    def get_nodes(self) -> dict[int, Node]:
        """Retourne les noeuds du modèle"""
        raise NotImplementedError

    @abstractmethod
    def get_elements(self) -> dict[int, Element]:
        """Retourne les éléments finis du modèle"""
        raise NotImplementedError

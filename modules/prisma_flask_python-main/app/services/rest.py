""" REST API Service """
from typing import TypeVar, Generic, List
from abc import ABCMeta, abstractmethod

T = TypeVar("T")


class RestAPI(Generic[T], metaclass=ABCMeta):
    """REST API Service"""

    @abstractmethod
    async def get_by_id(self, _id: int | str) -> T:
        """Get a single item by id"""
        raise NotImplementedError

    @abstractmethod
    async def get_all(self) -> List[T]:
        """Get all items"""
        raise NotImplementedError

    @abstractmethod
    async def create(self, data: dict) -> T:
        """Create a new item"""
        raise NotImplementedError

    @abstractmethod
    async def update(self, _id: int | str, data: dict) -> T:
        """Update an existing item"""
        raise NotImplementedError

    @abstractmethod
    async def delete(self, _id: int | str) -> None:
        """Delete an item"""
        raise NotImplementedError

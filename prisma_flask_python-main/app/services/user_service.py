"""User service module"""

from prisma.models import User
from app.prisma_client import PrismaManager
from app.services.rest import RestAPI


class UserService(RestAPI):
    """User service"""

    async def get_by_id(self, _id: int | str) -> User:
        """Get a single user by id"""
        async with PrismaManager() as prisma:
            user = await prisma.user.find_unique(where={"id": _id})

        return user

    async def get_all(self) -> list[User]:
        """Get all users"""
        async with PrismaManager() as prisma:
            users = await prisma.user.find_many()

        return users

    async def create(self, data: dict) -> User:
        """Create a new user"""
        async with PrismaManager() as prisma:
            user = await prisma.user.create(data=data)

        return user

    async def update(self, _id: int | str, data: User) -> User:
        """Update an existing user"""
        async with PrismaManager() as prisma:
            user = await prisma.user.update(where={"id": _id}, data=data)

        return user

    async def delete(self, _id: int | str) -> None:
        """Delete a user"""
        async with PrismaManager() as prisma:
            await prisma.user.delete(where={"id": _id})


# Create a singleton instance of the UserService
USERSERVICE = UserService()

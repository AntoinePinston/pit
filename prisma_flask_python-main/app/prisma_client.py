""" Prisma Client Manager """ ""
from prisma import Prisma


class PrismaManager:
    """Prisma Manager"""

    def __init__(self):
        """Initialize Prisma Manager"""
        self.prisma = Prisma()

    async def __aenter__(self):
        """Connect to Prisma"""
        await self.prisma.connect()
        return self.prisma

    async def __aexit__(self, exc_type, exc, tb):
        """Disconnect from Prisma"""
        await self.prisma.disconnect()

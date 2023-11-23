"""Main module."""

import asyncio
from app.services.user_service import USERSERVICE


async def main():
    """Main function"""

    name = input("What is your name? ")

    email = input("What is your email? ")

    data = {"name": name, "email": email}

    user = await USERSERVICE.create(data)

    print("User created: ", user)

    database_users = await USERSERVICE.get_all()

    print(database_users)


if __name__ == "__main__":
    asyncio.run(main())

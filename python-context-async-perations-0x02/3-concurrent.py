import asyncio
import aiosqlite

# async def async_fetch_users():
#     db = await aiosqlite.connect("users.db")
#     cursor = db.execute("SELECT * FROM users")
#     rows = cursor.fetchall()
#     await cursor.close()
#     await db.close()
#     return rows

async def async_fetch_users():
    async with aiosqlite.connect("users.db") as db:
        async with db.execute("SELECT * FROM users") as cursor:
            rows = await cursor.fetchall()
            return rows

# async def async_fetch_older_users():
#     db = await aiosqlite.connect("users.db")
#     cursor = await db.execute("SELECT * FROM users WHERE age > 40")
#     rows = await cursor.fetchall()
#     await cursor.close()
#     await db.close()
#     return rows

async def async_fetch_older_users():
    async with aiosqlite.connect("users.db") as db:
        async with db.execute("SELECT * FROM users WHERE age > 40") as cursor:
            rows = await cursor.fetchall()
            return rows

async def fetch_concurrently():
    all_user, all_user_o40 = await asyncio.gather(async_fetch_users(), async_fetch_older_users())

    print("All Users")
    for user in all_user:
        print(user)

    print("\nAll Users Above 40")
    for user in all_user_o40:
        print(user)

asyncio.run(fetch_concurrently())
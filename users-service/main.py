import os
import asyncpg
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# This API is public and stateless: it uses no cookies, sessions or Authorization
# header, so credentialed cross-origin requests are not allowed. Browsers reject
# the combination of allow_origins=["*"] with allow_credentials=True outright, so
# a wildcard origin is only valid while credentials stay off. If you later add
# authentication, replace "*" with the explicit frontend origin.
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=False,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Columns that are safe to expose over HTTP. "password" is deliberately absent:
# never let a SELECT * put a credential column into an API response.
USER_COLUMNS = 'id, email, name, role, "createdAt", "updatedAt"'


async def get_db_connection():
    return await asyncpg.connect(
        user=os.getenv("DB_USER", "user"),
        password=os.getenv("DB_PASSWORD", "password"),
        database=os.getenv("DB_NAME", "ecommerce_db"),
        host=os.getenv("DB_HOST", "database"),
        port=os.getenv("DB_PORT", "5432")
    )

@app.get("/users")
async def get_users():
    conn = await get_db_connection()
    try:
        rows = await conn.fetch(f'SELECT {USER_COLUMNS} FROM "User"')
        return [dict(row) for row in rows]
    finally:
        await conn.close()

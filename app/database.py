from fastapi import FastAPI
from sqlalchemy import MetaData, Table, Column, Integer, String
from databases import Database

app = FastAPI()

DATABASE_URL = "postgresql://username:password@localhost/dbname"
database = Database(DATABASE_URL)
metadata = MetaData()

items = Table(
    "items",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("name", String(50)),
    Column("description", String(100)),
)

@app.on_event("startup")
async def startup():
    await database.connect()

@app.on_event("shutdown")
async def shutdown():
    await database.disconnect()

@app.get("/items/")
async def read_items():
    query = items.select()
    return await database.fetch_all(query)

@app.get("/items/{item_id}")
async def read_item(item_id: int):
    query = f"SELECT * FROM items WHERE id = {item_id}"
    return await database.fetch_one(query)

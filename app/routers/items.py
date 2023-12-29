from fastapi import FastAPI
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import sessionmaker, declarative_base
from fastapi import APIRouter

router = APIRouter()
app = FastAPI()

DATABASE_URL = "postgresql://username:password@localhost/docker_project"
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

class Item(Base):
    __tablename__ = "items"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(50))
    description = Column(String(100))

Base.metadata.create_all(bind=engine)

@app.get("/items/")
def read_items():
    db = SessionLocal()
    items = db.query(Item).all()
    return items

@app.get("/items/{item_id}")
def read_item(item_id: int):
    db = SessionLocal()
    item = db.query(Item).filter(Item.id == item_id).first()
    return item

@router.get("/")
async def read_items():
    return {"message": "Read all items"}

@router.get("/{item_id}")
async def read_item(item_id: int):
    return {"message": f"Read item with ID {item_id}"}

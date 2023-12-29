from fastapi import FastAPI
from app import routers

app = FastAPI()

app.include_router(routers.items.router, prefix="/items")

if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="127.0.0.1", port=8000)


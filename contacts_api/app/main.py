from fastapi import FastAPI
from app.routers import contacts
from app.database import init_db

app = FastAPI()

@app.on_event("startup")
async def startup():
    await init_db()

app.include_router(contacts.router)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)

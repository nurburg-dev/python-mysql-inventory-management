from fastapi import FastAPI
import os
from dotenv import load_dotenv
from routes.item_routes import router as item_router

load_dotenv()

app = FastAPI(title="Inventory Management API", version="1.0.0")

app.include_router(item_router, prefix="/api")

if __name__ == "__main__":
    import uvicorn
    port = int(os.getenv("PORT", 8000))
    uvicorn.run(app, host="0.0.0.0", port=port)
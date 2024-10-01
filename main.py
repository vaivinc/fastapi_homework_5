from typing import Optional
from fastapi import FastAPI, Path, Header, Query
import uvicorn
from datetime import datetime

app = FastAPI()

@app.get("/path/{user_id}/")
async def index(user_id: int = Path(description="user_id"),
                timestamp: Optional[str] = Query(None),
                x_client_version: int = Header()):
    if not timestamp:
        timestamp = datetime.now().isoformat() #isoformat потрібен щоб преобразувати дату и час

    return {
        "user_id": user_id,
        "timestamp": timestamp,
        "X-Client-Version": x_client_version,
        "message": f"Hello, {user_id}!"
    }

if __name__ == "__main__":
    uvicorn.run("main:app", reload=True)

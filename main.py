from typing import Optional
from fastapi import FastAPI, Path, Header, Query
import uvicorn
from datetime import datetime

app = FastAPI()

@app.get("/path/{user_id}/")
async def index(user_id: int = Path(description="Enter your id, Example: 1"),
                timestamp: Optional[str] = Query(None, description="Enter your time, Example: 12:49"),
                x_client_version: int = Header(description="Enter your client_version, Example: 3.1.1")):
    if not timestamp:
        timestamp = datetime.now().isoformat()

    return {
        "user_id": user_id,
        "timestamp": timestamp,
        "X-Client-Version": x_client_version,
        "message": f"Hello, {user_id}!"
    }

if __name__ == "__main__":
    uvicorn.run("main:app", reload=True)

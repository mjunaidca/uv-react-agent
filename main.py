from fastapi import FastAPI, Request
from pydantic import BaseModel
from typing import Optional, Dict, Any
from enum import Enum
from datetime import datetime

# Define the status enum as per the API schema
class RunStatus(str, Enum):
    PENDING = "pending"
    ERROR = "error"
    SUCCESS = "success"
    TIMEOUT = "timeout"
    INTERRUPTED = "interrupted"

# Define the webhook payload schema
class WebhookPayload(BaseModel):
    run_id: str
    thread_id: str
    assistant_id: str
    created_at: datetime
    updated_at: datetime
    status: RunStatus
    metadata: Dict[str, Any]
    kwargs: Dict[str, Any]
    multitask_strategy: str

app = FastAPI()

@app.post("/webhook")
async def handle_webhook(payload: WebhookPayload):
    print("\n===== Webhook Received =====")
    print(f"Run ID: {payload.run_id}")
    print(f"Thread ID: {payload.thread_id}")
    print(f"Status: {payload.status}")
    print(f"Created at: {payload.created_at}")
    print(f"Updated at: {payload.updated_at}")
    print(f"Metadata: {payload.metadata}")
    print(f"Arguments: {payload.kwargs}")
    print("==========================\n")
    
    return {"message": "Webhook processed successfully"}

# For debugging/testing
@app.get("/")
async def root():
    return {"message": "Webhook server is running"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
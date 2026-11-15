from fastapi import APIRouter, Depends, HTTPException
from pydantic import BaseModel
from app.core.security import verify_api_key

router = APIRouter()

class PromptRequest(BaseModel):
    query: str

@router.post("/chat", dependencies=[Depends(verify_api_key)])
async def chat_with_ai(data: PromptRequest):
    return {
        "status": "success",
        "engine": "Nehansh AI Local",
        "received_query": data.query,
        "response": f"Pro server successfully processed: '{data.query}'"
    }

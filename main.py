from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from AIAgent import AIAgent 

app = FastAPI()
agent = AIAgent()

class StartChatRequest(BaseModel):
    message: str
    
class StartChatResponse(BaseModel):
    response: str 

import asyncio

@app.post("/chat", response_model=StartChatResponse)
async def start_chat(request: StartChatRequest):
    response = await agent.llm_call(request.message)
    if isinstance(response, str) and response.startswith("Error in LLM call:"):
        raise HTTPException(status_code=400, detail=response)
    return StartChatResponse(response=response)
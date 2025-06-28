from fastapi import FastAPI
from pydantic import BaseModel
from Backend.chat_handler import handle_user_message  

app = FastAPI()

class ChatRequest(BaseModel):
    message: str

@app.post("/chat")
async def chat(req: ChatRequest):
    response = await handle_user_message(req.message)
    return {"response": response}

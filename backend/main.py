from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI(title="Mini MediCare Pro WhatsApp Bot")


@app.get("/")
def home():
    return {
        "message": "Mini MediCare Pro WhatsApp Bot is running 🚀"
    }


@app.get("/health")
def health_check():
    return {
        "status": "healthy",
        "service": "Mini MediCare Pro WhatsApp Bot"
    }


class WhatsAppMessage(BaseModel):
    from_number: str
    message: str


@app.post("/webhook/whatsapp")
async def whatsapp_webhook(data: WhatsAppMessage):
    return {
        "status": "received",
        "message": "WhatsApp message received",
        "data": {
            "from_number": data.from_number,
            "message": data.message
        }
    }
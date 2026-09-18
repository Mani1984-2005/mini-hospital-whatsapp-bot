from pydantic import BaseModel


class Appointment(BaseModel):
    phone_number: str
    department: str
    doctor: str
    date: str
    time: str
    status: str = "confirmed"
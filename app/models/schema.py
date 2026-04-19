from pydantic import BaseModel

class RequestModel(BaseModel):
    base: str
    target: str
from pydantic import BaseModel, Field

class BasketCreateSchema(BaseModel):
    name: int = Field(ge=0)
    count: int = Field(ge=0)
    price: str
    user: str
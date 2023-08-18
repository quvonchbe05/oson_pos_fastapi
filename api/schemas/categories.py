from pydantic import BaseModel, Field

class CategorySchema(BaseModel):
    name: str = Field(max_length=155)
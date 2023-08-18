from pydantic import BaseModel, Field
from api.schemas.categories import CategorySchema


class ProductSchema(BaseModel):
    name: str = Field(max_length=200)
    amount: int
    price: str
    sale_price: str
    bar_code: str
    category_id: int
    

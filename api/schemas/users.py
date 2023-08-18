from pydantic import BaseModel, Field

class UserCreateSchema(BaseModel):
    name: str = Field(None, max_length=155)
    username: str = Field(..., max_length=155)
    email: str = Field(..., max_length=155)
    password: str = Field(..., min_length=8)

    
class UserEditSchema(BaseModel):
    name: str = Field(None, max_length=155)
    username: str = Field(..., max_length=155)
    email: str = Field(..., max_length=155)



from pydantic import BaseModel

class UserBase(BaseModel):
    username: str

class UserCreate(UserBase):
    pass

class UserRead(UserBase):
    id: int
    model_config = {"from_attributes": True}

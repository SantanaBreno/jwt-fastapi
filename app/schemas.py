import re
from pydantic import BaseModel, validator

class User(BaseModel):
    email: str
    password: str

    @validator('email')
    def validate_username(cls, value):
        if not re.match('^[a-z]|[0-9]|@+$', value):
            raise ValueError("email format invalid")
        return value
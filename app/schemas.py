import re
from pydantic import BaseModel, field_validator
from typing import Optional

class User(BaseModel):
    email: str
    password: str
    name: Optional[str] = None

    @field_validator('email')
    def validate_email(cls, value):
        # Regex para validação de email
        email_regex = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
        if not re.match(email_regex, value):
            raise ValueError("Invalid email format")
        return value

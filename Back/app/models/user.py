from pydantic import BaseModel

class User(BaseModel):
    id: str
    name: str
    accessibility_settings: dict  # Ex: {"font_size": 16, "high_contrast": True}
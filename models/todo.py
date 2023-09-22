from pydantic import BaseModel
from typing import Optional

class BaseId(BaseModel):
    id: int

class TodoSetable(BaseModel):
    title: str
    description: Optional[str] = None
    completed: bool = False

class Todo(BaseId, TodoSetable):
    class config:
        orm_mode = True
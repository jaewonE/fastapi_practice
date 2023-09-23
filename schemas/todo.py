from pydantic import BaseModel
from typing import Optional

from utils.typing import AllOptional

class BaseId(BaseModel):
    id: int

class TodoSetable(BaseModel):
    title: str
    description: Optional[str] = None
    completed: bool = False

class Todo(BaseId, TodoSetable):
    class Config:
        orm_mode = True

class TodoInput(TodoSetable):
    pass

class TodoUpdate(TodoSetable, metaclass=AllOptional):
    pass
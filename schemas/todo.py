from pydantic import BaseModel
from typing import Optional


from models.todo import TodoSetable
from utils.typing import AllOptional

class TodoInput(TodoSetable):
    pass

class TodoUpdate(TodoSetable, metaclass=AllOptional):
    pass
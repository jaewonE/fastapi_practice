from fastapi import APIRouter

from db import todo_list
from models.todo import Todo
from schemas.todo import TodoInput

router = APIRouter(
    prefix="",
    tags=[""],
    responses={404: {"description": "Not found"}},
)

@router.get("/")
async def root(limit: int = None):
    """
    예를 들어 /?limit=10 주소로 접속하면 limit는 10이 된다.
    """
    return_todo_list = todo_list[:limit] if limit != None else todo_list
    return {'todo_list': return_todo_list}


@router.post('/')
async def add_todo(todo: TodoInput):
    last_todo_id = todo_list[-1].id if len(todo_list) > 0 else 0
    new_todo = Todo.parse_obj({
        'id': last_todo_id + 1,
        **todo.dict(),
    })
    todo_list.append(new_todo)
    return {'append': new_todo}
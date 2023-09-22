from fastapi import APIRouter

from services.todo import TodoService
from schemas.todo import TodoUpdate

router = APIRouter(
    prefix="/todo",
    tags=["todo"],
    responses={404: {"description": "Not found"}},
)
todoService = TodoService()

@router.get("/{todo_id}")
async def get_todo(todo_id: int):
    if todo_id == None or todo_id < 0:
        return {"error": "todo_id is invalid"}
    return {"todo": todoService.find_todo_by_id(todo_id)}

@router.put("/{todo_id}")
async def update_todo(todo_id: int, updateTodo: TodoUpdate):
    if todo_id == None or todo_id < 0:
        return {"error": "todo_id is invalid"}
    return todoService.update_todo_by_id(todo_id, updateTodo)


@router.delete("/{todo_id}")
async def delete_todo(todo_id: int):
    if todo_id == None or todo_id < 0:
        return {"error": "todo_id is invalid"}
    return todoService.delete_todo_by_id(todo_id)
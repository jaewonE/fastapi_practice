from fastapi import APIRouter, HTTPException

from services.todo import TodoService
from schemas.todo import Todo, TodoInput, TodoUpdate

router = APIRouter(
    prefix="/todo",
    tags=["todo"],
    responses={404: {"description": "Not found"}},
)
todoService = TodoService()


@router.post("/", response_model=Todo)
def create_todo(todo:TodoInput):
    return todoService.create_todo(todo=todo)


@router.get("/", response_model=list[Todo])
async def get_todo_list():
    return todoService.get_todo_list()


@router.get("/{todo_id}", response_model=Todo)
async def get_todo(todo_id: int):
    todo = todoService.find_todo(todo_id=todo_id)
    if todo is None:
        raise HTTPException(status_code=404, detail="Todo not found")
    return todo


@router.put("/{todo_id}")
async def update_todo(todo_id: int, update_todo: TodoUpdate):
    return todoService.update_todo_by_id(todo_id, update_todo)


@router.delete("/{todo_id}")
async def delete_todo(todo_id: int):
    return todoService.delete_todo(todo_id)
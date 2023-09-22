from typing import Optional

from models.todo import Todo
from db import todo_list
from schemas.todo import TodoUpdate

class TodoService:
    def __init__(self):
        pass

    def _get_index_by_id(self, todo_id: int) -> Optional[int]:
        for i in range(len(todo_list)):
            if todo_list[i].id == todo_id:
                return i
        return None

    def find_todo_by_id(self, todo_id: int) -> Optional[Todo]:
        index = self._get_index_by_id(todo_id)
        if index == None:
            return None
        return todo_list[index]
    
    def update_todo_by_id(self, todo_id:int, updateTodo: TodoUpdate)->bool:
        index = self._get_index_by_id(todo_id)
        if index == None:
            return False
        updated_todo = Todo.parse_obj({
            **todo_list[index].dict(),
            **updateTodo.dict(),
        })
        print(updated_todo.dict())
        todo_list[index] = updated_todo
        return True

    def delete_todo_by_id(self, todo_id:int)->bool:
        index = self._get_index_by_id(todo_id)
        if index == None:
            return False
        todo_list.pop(index)
        return True

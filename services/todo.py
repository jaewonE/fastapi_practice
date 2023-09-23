from typing import Optional, List

from models.todo import Todo
from schemas.todo import TodoUpdate, TodoInput
from db import get_db_session

class TodoService:
    def __init__(self):
        self.model = Todo


    def create_todo(self, todo: TodoInput) -> Todo:
        db = get_db_session()
        try:
            new_todo = self.model(**todo.dict())
            db.add(new_todo)
            db.commit()
            db.refresh(new_todo)
            return new_todo
        except:
            db.rollback()
            raise Exception("Todo create failed")
    

    def get_todo_list(self, limit: int = None) -> List[Todo]:
        db = get_db_session()
        try:
            if limit == None:
                return db.query(self.model).all()
            return db.query(self.model).limit(limit).all()
        except Exception as e:
            return []


    def find_todo(self, todo_id: int) -> Optional[Todo]:
        db = get_db_session()
        try:
            return db.query(self.model).filter(self.model.id == todo_id).first()
        except:
            return []
    

    def update_todo_by_id(self, todo_id:int, todo_update: TodoUpdate)->bool:
        db = get_db_session()
        try:
            todo = db.query(self.model).filter(self.model.id == todo_id).first()
            if todo == None:
                return False
            
            for key, value in todo_update.dict(exclude_unset=True).items():
                setattr(todo, key, value)
            
            db.add(todo)
            db.commit()
            db.refresh(todo)
            return True
        except:
            db.rollback()
            raise Exception("Todo update failed")


    def delete_todo(self, todo_id: int) -> bool:
        db = get_db_session()
        try:
            todo = db.query(self.model).filter(self.model.id == todo_id).first()
            if todo == None:
                return False
            db.delete(todo)
            db.commit()
            return True
        except:
            db.rollback()
            raise Exception("Todo delete failed")

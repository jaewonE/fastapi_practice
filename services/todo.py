from typing import Optional, List
from sqlalchemy.orm import Session

from models.todo import Todo
from schemas.todo import TodoUpdate, TodoInput

class TodoService:
    def __init__(self):
        self.model = Todo

    def create_todo(self, db:Session, todo: TodoInput) -> Todo:
        new_todo = self.model(**todo.dict())
        db.add(new_todo)
        db.commit()
        db.refresh(new_todo)
        return new_todo
    
    def get_todo_list(self, db:Session, limit: int = None) -> List[Todo]:
        if limit == None:
            return db.query(self.model).all()
        return db.query(self.model).limit(limit).all()

    def find_todo(self, db: Session, todo_id: int) -> Optional[Todo]:
        return db.query(self.model).filter(self.model.id == todo_id).first()
    
    def update_todo_by_id(self, db:Session, todo_id:int, todo_update: TodoUpdate)->bool:
        todo = db.query(self.model).filter(self.model.id == todo_id).first()
        if todo == None:
            return False
        
        for key, value in todo_update.dict(exclude_unset=True).items():
            setattr(todo, key, value)
        
        db.add(todo)
        db.commit()
        db.refresh(todo)
        return True

    def delete_todo(self, db:Session, todo_id: int) -> bool:
        todo = db.query(self.model).filter(self.model.id == todo_id).first()
        if todo == None:
            return False
        db.delete(todo)
        db.commit()
        return True

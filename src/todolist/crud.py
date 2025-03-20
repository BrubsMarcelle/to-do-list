from sqlalchemy.orm import Session
from .models import Todo
from .schemas import TodoCreate

def get_todo(db: Session, todo_id: int):
    return db.query(Todo).filter(Todo.id == todo_id).first()

def get_all_todos(db: Session):
    return db.query(Todo).all()

def create_todo(db: Session, todo: TodoCreate):
    db_todo = Todo(**todo.dict())
    db.add(db_todo)
    db.commit()
    db.refresh(db_todo)
    return db_todo

def update_todo(db: Session, todo_id: int, updated_data: TodoCreate):
    todo = db.query(Todo).filter(Todo.id == todo_id).first()
    if todo:
        for key, value in updated_data.dict().items():
            setattr(todo, key, value)
        db.commit()
        db.refresh(todo)
    return todo

def delete_todo(db: Session, todo_id: int):
    todo = db.query(Todo).filter(Todo.id == todo_id).first()
    if todo:
        db.delete(todo)
        db.commit()
    return todo
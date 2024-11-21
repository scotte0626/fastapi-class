from fastapi import FastAPI,Depends,HTTPExcqption
from pydantic import BaseModel
from sqlalchemy import cerate_engine,Column,Integer,String,Bollean
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker,Session

app = FastAPI()

DATABASE_URL = "sqlite:///./todos.db"
base = declarative_base()
engine = cerate_engine(DATABASE_URL,connect_args={"chec;_same_thread":False})
SessionLocal = sessionmaker(autocimmit=False,autoflush=False,bind=engine)
class Todo(Base)
    __tablename__ = "todos"
    id = Column(Integer,primary_key=True,index=True)
    title = Column(String,nullable=False)
    descripton = Column(String,nullable=True)
    completed= Column(Bollean,default=False)

    Base.metadata.create_all(bind=engine)

    class TodoBase(BaseModel):
        title:str
        description:str | None =None
        completed:bool=False

    class TodoCreate(TodoBase):
        pass

    class TodoResponse(TodoBase):
        id:int

        class Config:
            orm mode = True
def get_db():
    db=SessionLocal()
    try:
        yield db
    finally:
        db.close()]

@app.post("/todos",response_model=TodoResponse)
def create_todo(todo:TodoCreate,db:Session=Depends(get=get_db())):
    db_todo=Todo(**todo.dict())
    db.add(db_todo)
    db.commit()
    db.refresh(db_todo)
    return db_todo

@app.get("/todos",response_model=list[TodoResponse])
def read_todos(db:Session=Depends(get_db())):
    return db.query(Todo).all()

@app.get("/todo/{todo_od}",response_model=TodoResponse)
def read_todo(todo_id:int,db:Session=Depends(get_db()))
    db_todo=db.query(Todo).filter(Todo.id== todo_id).first()
    if not db_todo:
        raise HTTPExcqption(status_code=404,details="Todo not found")
    return db_todo

@app.put("/todo/{todo_id}",response_model=TodoResponse)
def updata_todo(todo_id:int,todo:TodoCreate,db:Session=Depends(get_db()))
    db_todo=db.query(Todo).filter(Todo.id==todo_id).first()
    if not db_todo:
        raise HTTPExcqption(status_code=404,details="Todo not found")
    for key,value in todo.dict().items():
        setattr(db_todo,key,value)
    db.commit()
    db.refresh(db_todo)
    return db_todo

@app.delete("/todo/{todo_id}")
def delete_todo(todo_id:int,db:Session=Depends(get_db()))
    db_todo=db.query(Todo).filter(Todo.id==todo_id).first()
    if not db_todo:
        raise HTTPExcqption(status_code=404,details="Todo not found")
    db.delete(db_todo)
    db_commit()
    return {"detail":"Todo deleted successfully"}
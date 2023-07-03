from fastapi import FastAPI, status
from fastapi.exceptions import HTTPException
from models import Book
from database import engine
from sqlmodel import Session,select
from typing import Optional,List
import uvicorn
from fastapi.params import Depends

app=FastAPI()

session=Session(bind=engine)

#####################################################################

@app.get('/',status_code=status.HTTP_200_OK)
def home():
    return{"hello":"world"}

#############################################
@app.get('/books', response_model=List[Book],status_code=status.HTTP_200_OK)
async def get_all_books():
    statement = select(Book)
    results = session.exec(statement).all()
    return results

@app.post('/books', response_model=Book,status_code=status.HTTP_201_CREATED)
async def create_a_book(book:Book):
    new_book = Book(title=book.title, description=book.description)
    session.add(new_book)
    session.commit()
    return new_book
    
@app.get('/book/{book_id}', response_model=Book)
async def get_a_book(book_id:int):
    statement = select(Book).where(Book.id==book_id)
    result = session.exec(statement).first()
    if result == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)
    return result

@app.put('/book/{book_id}', response_model=Book)
async def update_a_book(book_id:int,book:Book):
    statement = select(Book).where(Book.id==book_id)
    result = session.exec(statement).first()
    result.title = book.title
    result.description = book.description
    session.commit()
    return result

@app.delete('/book/{book_id}', status_code=status.HTTP_204_NO_CONTENT)
async def delete_a_book(book_id:int):
    statement = select(Book).where(Book.id==book_id)
    result = session.exec(statement).one_or_none()
    if result == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail="Resource Not Found")
    session.delete(result)
    session.commit()
    return result

@app.get('/booktitle')
async def get_a_title(book_title:str,description:str):
    statement = select(Book).where(Book.title == book_title).where(Book.description == description)
    result = session.exec(statement).all()
    if result == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)
    return result

if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)


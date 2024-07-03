from fastapi import FastAPI
from schemas import Book


app = FastAPI()


@app.get("/books")
def get_book():
    book = Book(title="Martin Iden", writer="Djeck London", duration="idk",
                summary="from stupid to genius", genres="roman")

    return book


@app.post("/books")
def add_book(book: Book):
    return book


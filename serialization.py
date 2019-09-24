
from marshmallow import Schema, fields

class BookSchema(Schema):
    title = fields.Str()
    author = fields.Str()

class Book:
    def __init__(self, title, author, descriptions):
        self.title = title
        self.author = author
        self.descriptions = descriptions


book = Book("clean code", "Bob martin", "A book about writing clean code")

book_schema = BookSchema()
book_dict = book_schema.dump(book)

print(book_dict)
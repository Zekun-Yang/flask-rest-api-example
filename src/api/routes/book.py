from flask import Blueprint, request
from api.utils.responses import response_with
from api.utils import responses as resp 
from api.models.books import Book, BookSchema
from api.utils.database import db
from marshmallow import ValidationError

book_routes = Blueprint("book_routes", __name__)

@book_routes.route('/', methods=['POST'])
def create_book():
    try:
        data = request.get_json()
        book_schema = BookSchema()
        book = book_schema.load(data)
        result = book_schema.dump(book.create())
        return response_with(resp.SUCCESS_201, value={'book':result})
    except ValidationError as e:
        print(e)
        return response_with(resp.INVALID_INPUT_422)


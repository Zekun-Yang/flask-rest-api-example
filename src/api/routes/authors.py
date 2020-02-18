from flask import Blueprint
from flask import request
from api.utils.responses import response_with
from api.utils import responses as resp
from api.models.authors import Author, AuthorSchema
from api.utils.database import db
from marshmallow import ValidationError

author_routes = Blueprint("author_routes", __name__)

@author_routes.route('/', methods=['POST'])
def create_author():
    try:
        
        data = request.get_json()
        author_schema = AuthorSchema()
        author = author_schema.load(data)
        print(author)
        result = author_schema.dump(author.create())
        return response_with(resp.SUCCESS_201, value={"author": result})
    except ValidationError as e:
        print(e.messages)
        
        return response_with(resp.INVALID_INPUT_422)



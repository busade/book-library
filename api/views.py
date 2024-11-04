from flask_restx import Resource, Namespace,fields
from flask import request
from .model import Books 
from http import HTTPStatus
from datetime import datetime
from .utils import db


bookNamespace = Namespace("Book", description="This is a namespace for books library")
library_model= bookNamespace.model(
    "Books",{
        'id':fields.Integer(),
        "title": fields.String(required=True, description= "Title of book"),
        "author": fields.String(required =True, description = "Author/Authors of the book"),
        "genre": fields.String(required = True,description = "This  is the Genre of the book"),
        "publication_date":fields.Date(required = True, Description = "This is the date the book was published"),
        "availability_status":fields.String(required = True, Description = "This is the status of the book whether it is available or borrowed"),
        "edition" :fields.String(required = True,Description = "This is the book edition"),
        "Summary":fields.String(required = True, Description = "This provides an overall summary of what the book entails") 

    }

)


@bookNamespace.route('/books')
class Creation (Resource):
    @bookNamespace.marshal_with(library_model)
    @bookNamespace.expect(library_model)
    @bookNamespace.doc("This function creates a new book into the system ")
    def post (self):
        data = request.get_json()
        new_book = Books(
            title = data.get("title"),
            author = data.get("author"),
            genre =data.get("genre"),
            publication_date=datetime.strptime(data.get("publication_date"),"%Y-%m-%d").date(),
            availability_status = data.get("availability_status"),
            edition = data.get("edition"),
            Summary = data.get("Summary")
        )
        new_book.save()
        return  new_book, HTTPStatus.CREATED 
    
    @bookNamespace.marshal_with(library_model)
    @bookNamespace.doc("This function gets all book available in the system")
    def get (self):
        books = Books.query.all()
        return books, HTTPStatus.OK
        
    


@bookNamespace.route('/book/<int:id>')
class GetUpdateDelete (Resource):
    @bookNamespace.marshal_with(library_model)
    @bookNamespace.doc("This gets a particular book by id")
    def get (self, id) :
        """ Get book by id requires an id parameter"""
        book = Books.get_by_id(id)

        return book, HTTPStatus.OK
        
    

    @bookNamespace.marshal_with(library_model)
    @bookNamespace.doc( "This function updates a Book by its id")
    def put (self,id):
        book_to_update = Books.get_by_id(id)
        data=request.get_json()
        if data.get("title"):
            book_to_update.title = data.get("title")
        if data.get("author"):
            book_to_update.author = data.get("author")
        if data.get("genre"):
            book_to_update.genre =data.get("genre")
        if data.get("publication_date"):
            book_to_update.publication_date = datetime.strptime(data.get("publication_date"), "%Y-%m-%d").date()
        if data.get("availability_status"):
            book_to_update.availability_status = data.get("availability_status")
        if data.get("edition"):
            book_to_update.edition = data.get("edition")
        if data.get("Summary"):
            book_to_update.Summary = data.get("Summary")
        
        db.session.commit()
        return book_to_update,HTTPStatus.ACCEPTED

    @bookNamespace.doc("This function deletes a book by id")
    def delete(self,id):
        book_to_delete= Books.get_by_id(id)
        db.session.delete(book_to_delete)
        db.session.commit()
        return {"message": "book deleted successfully"}, HTTPStatus.OK

    
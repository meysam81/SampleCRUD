from http import HTTPStatus
from flask import jsonify, request, Response

from .app import app
from .serialize import book_schema, book_schemas
from .database import db, Book


@app.route("/books", methods=["GET", "POST"], provide_automatic_options=False)
def books():
    if request.method == "GET":
        books = Book.query.all()

        response = Response(
            book_schemas.dumps(books),
            status=HTTPStatus.OK,
            content_type="application/json",
        )

        return response

    if request.method == "POST":
        if not request.is_json:
            return 'Only json requests are accepted', HTTPStatus.BAD_REQUEST

        # validating user input
        book = book_schema.loads(request.data)

        db.session.add(Book(name=book["name"]))
        db.session.commit()

        return book, HTTPStatus.CREATED


@app.route("/books/<int:book_id>", methods=["GET", "PATCH", "DELETE"],
           provide_automatic_options=False)
def book(book_id: int):
    if request.method == "GET":
        book = Book.query.filter_by(id=book_id).first()
        if not book:
            return jsonify(f'Not Found: {book_id}'), HTTPStatus.NOT_FOUND

        response = Response(
            book_schema.dumps(book),
            status=HTTPStatus.OK,
            content_type="application/json",
        )

        return response

    if request.method == "DELETE":
        result = Book.query.filter_by(id=book_id).delete()
        db.session.commit()

        if result:
            return '', HTTPStatus.NO_CONTENT

        return jsonify(f'Not Found: {book_id}'), HTTPStatus.NOT_FOUND

    if request.method == "PATCH":
        if not request.is_json:
            return 'Only json requests are accepted', HTTPStatus.BAD_REQUEST

        book = book_schema.loads(request.data)

        result = Book.query.\
            filter_by(id=book_id).\
            update(book)
        db.session.commit()

        if result:
            response = Response(
                book,
                status=HTTPStatus.ACCEPTED,
                content_type="application/json",
            )
            return response

        return jsonify(f'Not Found: {book_id}'), HTTPStatus.NOT_FOUND

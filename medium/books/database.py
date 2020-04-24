from ..database import db


class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=True, nullable=False)

    def __repr__(self):  # pragma: no cover
        return f'<Book {self.name}>'

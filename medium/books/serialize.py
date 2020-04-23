from marshmallow import Schema, fields


class BookSchema(Schema):
    id = fields.Integer(dump_only=True)
    name = fields.String(required=True, data_key="bookName")


book_schema = BookSchema()
book_schemas = BookSchema(many=True)

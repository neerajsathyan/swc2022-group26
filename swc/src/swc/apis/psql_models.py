from flask_sqlalchemy import SQLAlchemy
from dataclasses import dataclass
from dataclasses_json import dataclass_json
from marshmallow import fields, Schema

db = SQLAlchemy()


@dataclass_json
@dataclass
class PlaceTable(db.Model):
    __tablename__ = 'place_table'
    # __table_args__ = {'schema': 'places'}

    id: int
    name: str
    description: str

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String())
    description = db.Column(db.String)
    thumbnail_url = db.Column(db.String)

    # class constructor
    def __init__(self, data):
        """
        Class constructor
        :param data:
        """
        self.name = data.get('name')
        self.description = data.get('description')

    def save(self):
        db.session.add(self)
        db.session.commit()

    def update(self, data):
        for key, item in data.items():
            setattr(self, key, item)
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    @staticmethod
    def get_all_places():
        return PlaceTable.query.all()

    @staticmethod
    def get_one_places(id):
        return PlaceTable.query.get(id)

    def __repr__(self):
        return "<Place %r>" % self.name


class PlaceTableSchema(Schema):
    id = fields.Int(required=True)
    name = fields.Str()
    description = fields.Str()

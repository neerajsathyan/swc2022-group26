from flask_sqlalchemy import SQLAlchemy
from dataclasses import dataclass
from dataclasses_json import dataclass_json

db = SQLAlchemy()


@dataclass_json
@dataclass
class PlaceTable(db.Model):
    __tablename__ = 'place_table'
    __table_args__ = {'schema': 'places'}

    id: int
    name: str
    description: str

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String())
    description = db.Column(db.String)
    thumbnail_url = db.Column(db.String)

    def __repr__(self):
        return "<Place %r>" % self.name

from .base import db


class Country(db.Model):
    __tablename__ = 'countries'

    id = db.Column(db.Integer, primary_key=True)
    wikiname = db.Column(db.String(96))
    slug = db.Column(db.String(32))
    name = db.Column(db.String(96))
    code = db.Column(db.String(5))
    currency = db.Column(db.String(32))

 
class City(db.Model):
    __tablename__ = 'cities'

    id = db.Column(db.Integer, primary_key=True)
    wikiname = db.Column(db.String(96))
    slug = db.Column(db.String(32))
    name = db.Column(db.String(96))
    rankings_1 = db.Column(db.Float)
    rankings_2 = db.Column(db.Float)
    rankings_3 = db.Column(db.Float)
    rankings_4 = db.Column(db.Float)
    total_ranking = db.Column(db.Float)
    timezone = db.Column(db.String(16))
    latitude = db.Column(db.Float)
    longitude = db.Column(db.Float)
    country_id = db.Column(db.Integer, db.ForeignKey('countries.id'))
    country = db.relationship('Country', backref=db.backref('cities', lazy='dynamic'))

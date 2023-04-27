from app import db

class Planet(db.Model):
    id = db.Column(db.Integer, primary_key=True, auto_incremet=True)
    name = db.Column(db.String(20), unique=True)
    description = db.Column(db.String(80))
    species = db.Column(db.Integer)
    weather = db.Column(db.String(80))
    distance_to_sun = db.Column(db.BigInteger)
    __tablename__ = 'planets'

    def planet_string(self):
        return f'{self.name}, {self.id}. Description:{self.description}'


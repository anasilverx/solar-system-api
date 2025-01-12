from app import db

class Planet(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(20))
    description = db.Column(db.String(80))
    species = db.Column(db.String(80))
    weather = db.Column(db.String(80))
    distance_to_sun = db.Column(db.BigInteger)
    __tablename__ = 'planets'

    def planet_string(self):
        return f'{self.name}, {self.id}. Description:{self.description}'

    def to_dict(self):
        return {   
                'id': self.id,
                'name': self.name,
                'description': self.description,
                'species': self.species,
                'weather': self.weather,
                'distance_to_sun': self.distance_to_sun
            }
    
    @classmethod
    def from_dict(cls, attribute_values):
        new_planet = cls(
            name=attribute_values['name'],
            description=attribute_values['description'],
            species=attribute_values['species'],
            weather=attribute_values['weather'],
            distance_to_sun=attribute_values['distance_to_sun'])
        return new_planet
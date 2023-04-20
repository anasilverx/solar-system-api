from flask import Blueprint, jsonify

class Planet:
    def __init__(self, id, name, description, moon):
        self.id = id #generate randmon id 
        self.name = name
        self.description = description
        self.moon = moon 

planets = [
    Planet(3, "Earth", "Third planet from sun", ["Moon"]),
    Planet(5, "Jupiter", "The largest in the solar system. Gas giant", ["Europa", "Io", "Elara"]),
    Planet(4, "Mars", "Third largest. Red Planet", ["Phobos", "Deimos"])
]

planets_bp = Blueprint("planets", __name__, url_prefix="/planets")
@planets_bp.route("", methods=["GET"])
def handle_books():
    planets_response = [vars(planets) for planet in planets]
    return jsonify(planets_response), 200
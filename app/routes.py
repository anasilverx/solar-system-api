from flask import Blueprint, jsonify, abort, make_response

class Planet:
    def __init__(self, id, name, description, moon):
        self.id = id 
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
def get_planets():
    return jsonify([vars(planet) for planet in planets]), 200

def validate_planets(planet_id):
    try:
        planet_id = int(planet_id)
    except:
        abort(make_response({"Error message":f"Planet id# {planet_id} invalid"}, 400))

    for planet in planets:
        if planet.id == planet_id:
            return vars(planet)
    
    abort(make_response({'Error message': f'Planet id# {planet_id} is not found'}, 404))

@planets_bp.route("/<planet_id>", methods=["GET"])
def get_planet(planet_id):
    return jsonify(validate_planets(planet_id)), 200
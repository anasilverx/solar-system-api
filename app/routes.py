from flask import Blueprint, jsonify, abort, make_response, request
from app import db
from app.models.planet import Planet

planets_bp = Blueprint('planets', __name__, url_prefix='/planets')

@planets_bp.route('', methods=['POST'])
def create_planet():
    request_body = request.get_json()
    if not 'name' or not 'description' or not 'species' or not 'weather' or not 'distance_to_sun':
        return 'Invalid Request', 400
    
    new_planet = Planet(
        name=request_body['name'],
        description=request_body['description'],
        species=request_body['species'],
        weather=request_body['weather'],
        distance_to_sun=request_body['distance_to_sun']
    )
    
    db.session.add(new_planet)
    db.session.commit()
    
    return make_response(f'Planet {new_planet.name} created'), 201

@planets_bp.route('', methods=['GET']) 
def get_planets():
    planets = Planet.query.all()
    planet_response = []
    for planet in planets:
        planet_response.append(
            {
                'name': planet.name,
                'description': planet.description,
                'species': planet.species,
                'weather': planet.weather,
                'distance_to_sun': planet.distance_to_sun
            }
        )
    
    return jsonify(planet_response), 200

# class Planet:
#     def __init__(self, id, name, description, moon):
#         self.id = id 
#         self.name = name
#         self.description = description
#         self.moon = moon 

# planets = [
#     Planet(3, "Earth", "Third planet from sun", ["Moon"]),
#     Planet(5, "Jupiter", "The largest in the solar system. Gas giant", ["Europa", "Io", "Elara"]),
#     Planet(4, "Mars", "Third largest. Red Planet", ["Phobos", "Deimos"])
# ]

# planets_bp = Blueprint("planets", __name__, url_prefix="/planets")
# @planets_bp.route("", methods=["GET"])
# def get_planets():
#     return jsonify([vars(planet) for planet in planets]), 200

# def validate_planets(planet_id):
#     try:
#         planet_id = int(planet_id)
#     except:
#         abort(make_response({"Error message":f"Planet id# {planet_id} invalid"}, 400))

#     for planet in planets:
#         if planet.id == planet_id:
#             return vars(planet)
    
#     abort(make_response({'Error message': f'Planet id# {planet_id} is not found'}, 404))

# @planets_bp.route("/<planet_id>", methods=["GET"])
# def get_planet(planet_id):
#     return jsonify(validate_planets(planet_id)), 200
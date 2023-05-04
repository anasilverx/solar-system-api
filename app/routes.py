from flask import Blueprint, jsonify, abort, make_response, request
from app import db
from app.models.planet import Planet

planets_bp = Blueprint('planets', __name__, url_prefix='/planets')

# helper function:
def validate_planet(planet_id):
    if not planet_id.isnumeric():
        abort(make_response({'msg': f'Invalid id. {planet_id} is not a number'}, 400))
    # planet_id = int(planet_id)
    planet = Planet.query.get(int(planet_id))
    
    if not planet:
        abort(make_response({'msg': f'Planet {planet_id} is not found'}, 404))
    
    return planet


# routes:
@planets_bp.route('', methods=['POST'])
def create_planet():
    request_body = request.get_json()
    if not 'name' in request_body or not 'description' in request_body or not 'species' in request_body or not 'weather' in request_body or not 'distance_to_sun' in request_body:
        return make_response({'msg':'Invalid Request'}), 400
    
    new_planet = Planet(
        name=request_body['name'],
        description=request_body['description'],
        species=request_body['species'],
        weather=request_body['weather'],
        distance_to_sun=request_body['distance_to_sun']
    )
    
    db.session.add(new_planet)
    db.session.commit()
    
    return make_response({'msg': f'Planet {new_planet.name} created'}), 201

@planets_bp.route('', methods=['GET']) 
def get_planets():
    name_query = request.args.get("name")

    if name_query:
        planets = Planet.query.filter_by(name=name_query.strip())
    else:
        planets = Planet.query.all()
    planet_response = []
    for planet in planets:
        planet_response.append(planet.to_dict())
    
    return jsonify(planet_response), 200

@planets_bp.route('/<planet_id>', methods=['GET'])
def get_one_planet(planet_id):
    planet = validate_planet(planet_id)
    
    return planet.to_dict(), 200

@planets_bp.route('/<planet_id>', methods=['PUT'])
def replace_one_planet(planet_id):
    planet = validate_planet(planet_id)
    request_body = request.get_json()
    
    planet.name = request_body.get("name", planet.name)
    planet.description = request_body.get("description", planet.description)
    planet.species = request_body.get("species", planet.species)
    planet.weather = request_body.get("weather", planet.weather)
    planet.distance_to_sun = request_body.get("distance_to_sun", planet.distance_to_sun)
    
    db.session.commit()
    
    return make_response({'msg': f"Planet with id {planet_id} was replaced successfully."}), 200

@planets_bp.route('/<planet_id>', methods=['DELETE'])
def delete_one_planet(planet_id):
    planet = validate_planet(planet_id)
    
    db.session.delete(planet)
    db.session.commit()
    
    return make_response({'msg': f"Planet with id {planet_id} was deleted successfully."}), 200
    

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
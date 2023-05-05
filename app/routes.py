from flask import Blueprint, jsonify, abort, make_response, request
from app import db
from app.models.planet import Planet

planets_bp = Blueprint('planets', __name__, url_prefix='/planets')

# helper function:
def validate_model(model, id):
    if not id.isnumeric():
        abort(make_response({'msg': f'Invalid id. {id} is not a number'}, 400))
    
    record = model.query.get(int(id))
    
    if not record:
        abort(make_response({'msg': f'{model.__name__} {id} is not found'}, 404))
    
    return record


# routes:
@planets_bp.route('', methods=['POST'])
def create_planet():
    request_body = request.get_json()
    #keep name and description as not optional
    if not 'name' in request_body or not 'description' in request_body or not 'species' in request_body or not 'weather' in request_body or not 'distance_to_sun' in request_body:
        return {'msg':'Invalid Request'}, 400
    
    new_planet = Planet.from_dict(request_body)
    
    db.session.add(new_planet)
    db.session.commit()
    
    return {'msg': f'Planet {new_planet.name} created'}, 201

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
    planet = validate_model(Planet, planet_id)
    
    return planet.to_dict(), 200

@planets_bp.route('/<planet_id>', methods=['PUT'])
def replace_one_planet(planet_id):
    planet = validate_model(Planet, planet_id)
    request_body = request.get_json()
    
    planet.name = request_body.get("name", planet.name)
    planet.description = request_body.get("description", planet.description)
    planet.species = request_body.get("species", planet.species)
    planet.weather = request_body.get("weather", planet.weather)
    planet.distance_to_sun = request_body.get("distance_to_sun", planet.distance_to_sun)
    
    db.session.commit()
    
    return {'msg': f"Planet with id {planet_id} was replaced successfully."}, 200

@planets_bp.route('/<planet_id>', methods=['DELETE'])
def delete_one_planet(planet_id):
    planet = validate_model(Planet, planet_id)
    
    db.session.delete(planet)
    db.session.commit()
    
    return {'msg': f"Planet with id {planet_id} was deleted successfully."}, 200
import pytest
from app import create_app
from app import db
from flask.signals import request_finished
from app.models.planet import Planet

@pytest.fixture
def app():
    app = create_app({"TESTING": True})

    @request_finished.connect_via(app)
    def expire_session(send, response, **extra):
        db.session.remove()

    with app.app_context():
        db.create_all()
        yield app
    
    with app.app_context():
        db.drop_all()

@pytest.fixture
def client(app):
    return app.test_client()

#Testing Data
@pytest.fixture
def three_planets(app):
    planet_one = Planet(
        id=1, 
        name="Mars", 
        description="red planet, third largest",
        species="martian",
        weather="extremely sunny",
        distance_to_sun=143000000000)
    planet_two = Planet(
        id=2, 
        name="Jupiter", 
        description="gas giant, largest in solar system",
        species="legitos",
        weather="stormy",
        distance_to_sun=484000000000)
    planet_three = Planet(
        id=3, 
        name="Earth", 
        description="suitable for breathing",
        species="human",
        weather="habitable",
        distance_to_sun=93000000000)
    
    db.session.add_all([planet_one, planet_two, planet_three])
    db.session.commit()
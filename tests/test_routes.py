def test_get_planets_empty_db_returns_empty_list(client):
    response = client.get('/planets')
    response_body = response.get_json()
    
    assert response.status_code == 200
    assert response_body == []
    
def test_get_one_planet_empty_db(client):
    response = client.get('/planets/1')
    response_body = response.get_json()
    
    assert response.status_code == 404
    assert response_body == {"msg": "Planet 1 is not found"}

def test_create_planet_adds_planet_to_db(client):
    response = client.post('/planets', json={
        "name": "test",
        "species": "creatures",
        "weather": "rainy",
        "distance_to_sun": 578000000,
        "description": "not habitable"})
    response_body = response.get_json()
    
    assert response.status_code == 201
    assert response_body == {"msg": "Planet test created"}

def test_get_one_planet_populated_db(client, three_planets):
    response = client.get('/planets/1')
    response_body = response.get_json()
    
    assert response.status_code == 200
    assert response_body == {
        "id": 1,
        "name": "Mars",
        "species": "martian",
        "weather": "extremely sunny",
        "distance_to_sun": 143000000000,
        "description": "red planet, third largest"}  

def test_get_all_planets_populated_db(client, three_planets):
    response = client.get('/planets')
    response_body = response.get_json()

    assert response_body == [
        {
            'id':1, 
            'name':"Mars", 
            'description':"red planet, third largest",
            'species':"martian",
            'weather':"extremely sunny",
            'distance_to_sun':143000000000
        },
        {
            'id':2, 
            'name':"Jupiter", 
            'description':"gas giant, largest in solar system",
            'species':"legitos",
            'weather':"stormy",
            'distance_to_sun':484000000000
        },
        {
            'id':3, 
            'name':"Earth", 
            'description':"suitable for breathing",
            'species':"human",
            'weather':"habitable",
            'distance_to_sun':93000000000
        }      
    ]
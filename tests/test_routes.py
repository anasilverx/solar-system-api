def test_get_planets_returns_empty_list_if_empty_db(client):
    response = client.get('/planets')
    response_body = response.get_json()
    
    assert response.status_code == 200
    assert response_body == []
    
def test_get_one_planet_when_empty_db(client):
    response = client.get('/planets/1')
    response_body = response.get_json()
    
    assert response.status_code == 404
    assert response_body == {"msg": "Planet 1 is not found"}
    
def test_create_planet_adds_planet_to_db(client, json={"name": "test",
"species": "",
"weather": "hjk",
"distance_to_sun": 57858,
"description": "cgj"}):
    response = client.post('/planets')
    response_body = response.get_json()
    
    assert response.status_body == 201
    assert response_body == {"msg": "Planet test created"}

def test_get_one_planet_when_empty_db(client, <fixture function that creates a record>):
    response = client.get('/planets/1')
    response_body = response.get_json()
    
    assert response.status_code == 200
    assert response_body == {<planet info from fixture function>}  

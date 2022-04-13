from ..src import app as flask_app, getdistance, getRoute, gasStations

def test_good_distance():
    with flask_app.test_client() as c:
        home = "Stuttgart"
        work = "Böblingen"
        rv = c.post('/distance', json={
            'homeLocation': home,
            'workingLocation': work
        })
        answer = getdistance()
        assert "Stunden" in answer and "Km" in answer

def test_bad_distance():
    with flask_app.test_client() as c:
        home = "Stutsdhd"
        work = "Böblingen"
        rv = c.post('/distance', json={
            'homeLocation': home,
            'workingLocation': work
        })
        answer = getdistance()
        assert "Mindestens eine der Angaben ist kein valider Ort" in answer

def test_bad_route():
    with flask_app.test_client() as c:
        home = "Hochdahl"
        work = "Ratingen"
        rv = c.post('/route', json={
            'homeLocation': home,
            'workingLocation': work
        })
        answer = getRoute()
        assert "folgende" in answer and "Route" in answer

def test_bad_route():
    with flask_app.test_client() as c:
        home = "sdhgoisvh"
        work = "Ratingen"
        rv = c.post('/route', json={
            'homeLocation': home,
            'workingLocation': work
        })
        answer = getRoute()
        assert "Mindestens eine der Angaben ist kein valider Ort" in answer

def test_good_gas():
    with flask_app.test_client() as c:
        home = "Stuttgart"
        fuel = "Benzin"
        rv = c.post('/distance', json={
            'homeLocation': home,
            'gasolineType': fuel
        })
        answer = gasStations()
        assert "Tankstellen" in answer and "Stadt" in answer

def test_bad_gas():
    with flask_app.test_client() as c:
        home = "adfv"
        fuel = "Diesel"
        rv = c.post('/distance', json={
            'homeLocation': home,
            'gasolineType': fuel
        })
        answer = gasStations()
        assert "Kein valider Ort angegeben" in answer
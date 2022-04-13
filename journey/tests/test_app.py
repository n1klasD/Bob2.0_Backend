from .. src import app as flask_app, get_Route

def test_good_route():
    with flask_app.test_client() as c:
        home = "Stuttgart"
        work = "Böblingen"
        rv = c.post('/distance', json={
            'homeLocation': home,
            'workingLocation': work
        })
        answer = get_Route()
        assert "Stunden" in answer and "Km" in answer
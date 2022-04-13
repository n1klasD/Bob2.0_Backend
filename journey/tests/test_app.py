from ..src import app as flask_app, getdistance

def test_good_route():
    with flask_app.test_client() as c:
        home = "Stuttgart"
        work = "Böblingen"
        rv = c.post('/distance', json={
            'homeLocation': home,
            'workingLocation': work
        })
        answer = getdistance()
        assert "Stunden" in answer and "Km" in answer
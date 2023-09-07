# helpers/results.py
from client.entities.entity import Session
from client.entities.results import Result, ResultSchema
def showresults():
    session = Session()
    results = session.query(Result).all()
    schema = ResultSchema(many=True)
    results = schema.dump(results)
    session.close()
    return results
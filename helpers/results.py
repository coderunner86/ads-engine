# helpers/results.py
from entities.entity import Session
from entities.results import Result, ResultSchema
def showresults():
    session = Session()
    results = session.query(Result).all()
    schema = ResultSchema(many=True)
    results = schema.dump(results)
    session.close()
    return results

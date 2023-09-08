#helpers/submit.py
from entities.entity import Session
from entities.results import Result
from flask import request
def submitaction():
    action = request.form.get('action')
    print('action', action)
    if action in ['accept', 'reject']:
        last_id = request.form.get('last_id')
        print('last_id', last_id)
        session = Session()
        result = session.query(Result).filter_by(id=last_id).first()
        print('result', result)
        if result:
            result.status = action
            session.commit()
        session.close()

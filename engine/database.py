# helpers/database.py
from client.entities.entity import Session
from client.entities.results import Result

def save_recommendation(user_input, ad_text):
    result = Result(
        ai_copy=ad_text,
        status="success",
        created_by="user",
        last_updated_by="user"
    )
    session = Session()
    session.add(result)
     # Flush the session to persist the object and get the last inserted ID
    session.flush()

    # Access the ID attribute of the inserted result
    last_id = result.id
    session.commit()
    return last_id

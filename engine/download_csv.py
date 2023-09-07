import os

from client.entities.entity import Session
from client.entities.results import Result, ResultSchema
from flask import make_response

def download_csv():
    session = Session()
    ads = session.query(Result.ai_copy, Result.status).all()
    session.close()

    csv_string = ','.join(['ID', 'AI Copy', 'Status']) + '\n'
    if ads:
        for ad in ads:
            csv_string += ','.join([str(ad[0]), str(ad[1] if ad[1] is not None else '')]) + '\n'


    data_dir = 'data' 
    csv_filename = 'ads_train.csv'

    csv_path = os.path.join(data_dir, csv_filename)

    with open(csv_path, 'w') as csv_file:
        csv_file.write(csv_string)


    response = make_response(csv_string)
    response.headers['Content-Type'] = 'text/csv'
    response.headers['Content-Disposition'] = 'attachment; filename=ads_train.csv'
    return response
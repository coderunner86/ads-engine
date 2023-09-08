import os
import sys 

entity_path = os.path.join(os.path.dirname(__file__), '..', 'entity')
sys.path.append(entity_path)

from flask import Flask, request, redirect, url_for, render_template
from flask_bootstrap import Bootstrap5
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, Length
from flask_cors import CORS

from client.entities.entity import engine, Base

from client.engine.open_ai_request import get_openai_response
from client.engine.database import save_recommendation
from client.engine.download_csv import download_csv

from client.helpers.results import showresults
from client.helpers.submit import submitaction

app = Flask(__name__)
app.secret_key = '&f2S4c./kdw3SG450xs#FR!'  
bootstrap = Bootstrap5(app)
CORS(app)
Base.metadata.create_all(engine)
@app.errorhandler(404)
def not_found_error(error):
    return render_template('404.html'), 404

@app.errorhandler(500)
def internal_error(error):
    return render_template('500.html'), 500

import logging
app.logger.setLevel(logging.ERROR)

class MyForm(FlaskForm):
    query = StringField('Which audience is your favorite?', validators=[DataRequired(), Length(min=5, max=50)])
    submit = SubmitField('Submit')

@app.route('/', methods=['GET'])
def home():
    return render_template('index.html')

@app.route('/search', methods=['GET', 'POST'])
def search_engine():
    form = MyForm()
    form.validate_on_submit()
    query=form.query.data
    return render_template('search.html', form=form)

@app.route('/match_audience', methods=['GET','POST'])
def match_audience():
    try:
        user_input = request.form.get('query')
        ad_text = get_openai_response(user_input)
        last_id = save_recommendation(user_input, ad_text)
        return render_template('match_audience.html', keywords=user_input, user_input=user_input, ad_text=ad_text, last_id=last_id)
    except Exception as e:
        error_message = str(e)
        return render_template('error.html', error_message=error_message)
    
@app.route('/submit_action', methods=['POST'])
def submit_action():
    submitaction()
    return redirect('/results')

@app.route('/results', methods=['GET'])
def show_results():
    results = showresults()
    return render_template('show_results.html', results=results)

@app.route('/download_csv')
def download_csv_file():
    response = download_csv()
    return response

if __name__ == '__main__':
    app.run(port=5001, debug=False)

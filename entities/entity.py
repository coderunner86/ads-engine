# coding=utf-8

from datetime import datetime
from sqlalchemy import create_engine, Column, String, Integer, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
#mysql://lzacjlvbwvek7ruo:qv899q7jdqolsuyo@ao9moanwus0rjiex.cbetxkdyhwsb.us-east-1.rds.amazonaws.com:3306/gj7n74l4z1idmjii
db_url = 'ao9moanwus0rjiex.cbetxkdyhwsb.us-east-1.rds.amazonaws.com:3306'
db_name = 'gj7n74l4z1idmjii'
db_user = 'lzacjlvbwvek7ruo'
db_password = 'qv899q7jdqolsuyo'
engine = create_engine(f'mysql://{db_user}:{db_password}@{db_url}/{db_name}')
Session = sessionmaker(bind=engine)

Base = declarative_base()

class Entity():
    id = Column(Integer, primary_key=True)
    created_at = Column(DateTime)
    updated_at = Column(DateTime)
    last_updated_by = Column(String)

    def __init__(self, created_by, last_updated_by):
        self.created_at = datetime.now()
        self.updated_at = datetime.now()
        self.last_updated_by = last_updated_by

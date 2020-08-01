from sqlalchemy import create_engine
from sqlalchemy_utils import create_database, database_exists
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
#from sqlalchemy import MetaData
#import os
from wtforms import *
from pprint import pprint

app = Flask(__name__)
app.debug = False
#app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:abc123@127.0.0.1:3306/CSC_5'
#for non-Garrett people use below for local host db
# app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:@127.0.0.1:3306/CSC_4'


app.config['SECURITY_REGISTERABLE'] = True
app.config['SECURITY_PASSWORD_SALT'] = 'mysalt'
app.config['SECURITY_SEND_REGISTER_EMAIL'] = False

app.config['ENV'] = 'development'
#app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:@127.0.0.1:3306/CSC_3'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False #to suppress warning
app.config['SQLALCHEMY_ECHO'] = True  # to print out SQL queries
app.secret_key ='replace later'
# db = SQLAlchemy(app)#

# conn = db.session.get_bind()
# meta = MetaData(conn)
# meta.reflect()

proto = 'mysql'
user = 'root'
password = ''
host = '127.0.0.1'
port = '3306'

# This engine just used to query for list of databases
mysql_engine = create_engine('{0}://{1}:{2}@{3}:{4}'.format(proto, user, password, host, port))
pprint(mysql_engine)

# Query for existing databases
existing_databases = mysql_engine.execute("SHOW DATABASES;")
# Results are a list of single item tuples, so unpack each tuple
existing_databases = [d[0] for d in existing_databases]

pprint(existing_databases)

# use this to select the database you want to use
# it will be created if it does not exist
database = 'CSC_4'
url = '{0}://{1}:{2}@{3}:{4}/{5}'.format(proto,
                                         user, password, host, port, database)
#app.config['SQLALCHEMY_DATABASE_URI'] = f'mysql://root:@127.0.0.1:3306/{database}'
app.config['SQLALCHEMY_DATABASE_URI'] = url

# Create database if not exists
if database not in existing_databases:
    mysql_engine.execute("CREATE DATABASE {0}".format(database))
    print("Created database {0}".format(database))
else:
    print("Did NOT create database, {database} already exists.")
#test code - 

if not database_exists(url):
    create_database(url)

#end test code -

# Go ahead and use this engine
db_engine = create_engine(url)
pprint(db_engine)

db = SQLAlchemy(app)
pprint(db)

from flask_sqlalchemy import SQLAlchemy
from flask import Flask

#Initiaze app and database connection
app = Flask(__name__)

#Configuring MySQL database
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqlconnector://UTSPemweb_notwouldby:a775ce8801b476528676d517b55c48a87407831c@nahkj.h.filess.io:3306/UTSPemweb_notwouldby'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

app.app_context().push()

from flask_sqlalchemy import SQLAlchemy
from flask import Flask

#Initiaze app and database connection
app = Flask(__name__)

#Configuring MySQL database
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqlconnector://PemwebUTS_writtenits:5c37e90d0620616381e1cf3e0e5aa5ff79b7e2ee@dco2x.h.filess.io:3307/PemwebUTS_writtenits'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

app.app_context().push()

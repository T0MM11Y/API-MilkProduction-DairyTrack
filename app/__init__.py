from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_jwt_extended import JWTManager

#local
app = Flask(__name__)
app.config['JWT_SECRET_KEY'] = 'tsth2'
app.config['JWT_ACCESS_TOKEN_EXPIRES'] = 3600
jwt = JWTManager(app)
app.config['SECRET_KEY'] = ''
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root@localhost/dairy_track'

#public
# app = Flask(__name__)
# app.config['SECRET_KEY'] = ''
# app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://if0_38474743:Tomm4145@sql307.infinityfree.com:3306/if0_38474743_dairy_track'

db = SQLAlchemy(app)

from app.models import Farmer, Cow , RawMilk, Supervisor, Admin
from app.routes import farmers_bp, cows_bp, raw_milks_bp, supervisors_bp, admins_bp, auth_bp



app.register_blueprint(farmers_bp, url_prefix='/api')
app.register_blueprint(cows_bp, url_prefix='/api')
app.register_blueprint(raw_milks_bp, url_prefix='/api')
app.register_blueprint(supervisors_bp, url_prefix='/api')
app.register_blueprint(admins_bp, url_prefix='/api')
app.register_blueprint(auth_bp)

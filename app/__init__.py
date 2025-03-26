from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_jwt_extended import JWTManager
from flask_cors import CORS  # Import CORS

#local
app = Flask(__name__)
app.config['JWT_SECRET_KEY'] = 'tsth2'
app.config['JWT_ACCESS_TOKEN_EXPIRES'] = 3600
jwt = JWTManager(app)
# app.config['SECRET_KEY'] = ''
# app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root@localhost/dairy_track'

#public
app.config['SECRET_KEY'] = ''
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://dairytrack_operation:c89d2e129b1b9d76b283c5989a33ef05f9cb88d2@d2pug.h.filess.io:61002/dairytrack_operation'

db = SQLAlchemy(app)

# Enable CORS for the app and specify allowed origins, methods, and headers
CORS(app, resources={r"/api/*": {"origins": "http://localhost:3000", "methods": ["GET", "POST", "PUT", "DELETE", "OPTIONS"], "allow_headers": ["Content-Type", "Authorization"]}})

from app.models import Farmer, Cow , RawMilk, Supervisor, Admin
from app.routes import farmers_bp, cows_bp, raw_milks_bp, supervisors_bp, admins_bp, auth_bp

app.register_blueprint(farmers_bp, url_prefix='/api')
app.register_blueprint(cows_bp, url_prefix='/api')
app.register_blueprint(raw_milks_bp, url_prefix='/api')
app.register_blueprint(supervisors_bp, url_prefix='/api')
app.register_blueprint(admins_bp, url_prefix='/api')
app.register_blueprint(auth_bp)
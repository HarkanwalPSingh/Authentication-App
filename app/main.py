from flask import Flask
from flask import jsonify
from flask import request

from flask_jwt_extended import create_access_token
from flask_jwt_extended import get_jwt_identity
from flask_jwt_extended import jwt_required
from flask_jwt_extended import JWTManager

from sqlalchemy.orm import Session

from app.crud import get_password

import config
from database import SessionLocal, engine
import crud, models

app = Flask(__name__)

app.config["JWT_SECRET_KEY"] = config.JWTSettings.JWT_SECRET_KEY
jwt = JWTManager(app)

models.Base.metadata.create_all(bind=engine)

# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()



@app.route("/login", methods=["POST"])
def login(db: Session = Depends(get_db)):
    username = request.json.get("username", None)
    password = request.json.get("password", None)
    db_pass = get_password()

from datetime import date
from sqlalchemy.orm import Session
import models

def get_user_id(db: Session, email: str):
    return db.query(models.User).filter(models.User.email == email).first()

def get_password(db: Session, email: str):
    return db.query(models.User.password).filter(models.User.email == email).first()
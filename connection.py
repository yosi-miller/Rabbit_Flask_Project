from sqlalchemy import create_engine
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import scoped_session, sessionmaker

from models import *

DB_URL = "postgresql://postgres:12345678@localhost/shopping_db"
engine = create_engine(DB_URL)
db_session = scoped_session(sessionmaker(autocommit=False, # don't commit changes'
                                         autoflush=False,
                                         bind=engine))

def init_db():
    import models
    Base.metadata.create_all(bind=engine)


def initialize_data():
    # בדוק אם קיימת רשומת דוא"ל בטבלת SingUpModel
    if not db_session.query(SingUpModel).filter_by(email="test@example.com").first():
        new_signup = SingUpModel(email="test@example.com")
        db_session.add(new_signup)

    # בדוק אם קיים קוד קופון בטבלת CouponCodeModel
    if not db_session.query(CouponCodeModel).filter_by(price=100).first():
        new_coupon = CouponCodeModel(price=100)
        db_session.add(new_coupon)

    # בדוק אם קיימת פריט בטבלת ItemsModel
    if not db_session.query(ItemsModel).filter_by(name="Shoes").first():
        new_item = ItemsModel(name="Shoes", amount=50)
        db_session.add(new_item)

    if not db_session.query(ItemsModel).filter_by(name="Shirt").first():
        new_item = ItemsModel(name="Shirt", amount=50)
        db_session.add(new_item)

    if not db_session.query(ItemsModel).filter_by(name="tour_ticket").first():
        new_item = ItemsModel(name="tour_ticket", amount=50)
        db_session.add(new_item)

    try:
        # שמירה על השינויים בבסיס הנתונים
        db_session.commit()
    except IntegrityError:
        # במקרה של שגיאה (כמו שכבר קיימת הרשומה), התעלם ואל תבצע commit נוסף
        db_session.rollback()
        print("Data already exists, no changes made.")

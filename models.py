from sqlalchemy import String, Column, Integer, Date, Table, ForeignKey, Float
from sqlalchemy.orm import declarative_base

Base = declarative_base()


class SingUpModel(Base):
    __tablename__ = 'signup'

    id = Column(Integer, primary_key=True)
    email = Column(String)


class CouponCodeModel(Base):
    __tablename__ = 'coupon_code'

    id = Column(Integer, primary_key=True)
    price =Column(Integer)


class ItemsModel(Base):
    __tablename__ = 'items'

    item_id = Column(Integer, primary_key=True)
    name = Column(String)
    amount = Column(Integer)

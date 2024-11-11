from connection import db_session
from models import SingUpModel, ItemsModel


def register_email(email):
    signup = db_session.query(SingUpModel).filter(SingUpModel.email == email).first()
    if signup:
        return False, f"Email: {email} already registered"

    else:
        new_signup = SingUpModel(email=email)
        db_session.add(new_signup)
        db_session.commit()
        return True, f"{new_signup.email} registered successfully"

def check_inventory(data):
    check_email = db_session.query(SingUpModel).filter(SingUpModel.email == data['email']).first()
    if not check_email:
        return False, f"Email: {data['email']} not registered"

    check_inventory = db_session.query(ItemsModel).filter(ItemsModel.item_id == data['item_id']).first()

    if check_inventory:
        if check_inventory.amount >= data['amount']:
            return True, f"Inventory check passed for item_id: {data['item_id']}"
        else:
            return False, f"Not enough inventory for item_id: {data['item_id']}"

from flask import Flask

from blueprint import action_bp
from connection import init_db, DB_URL, db_session, initialize_data

app = Flask(__name__)

# Configure SQLAlchemy
app.config["SQLALCHEMY_DATABASE_URI"] = DB_URL
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

with app.app_context():
    initialize_data()
    init_db()

app.register_blueprint(action_bp)

# Teardown for database session
@app.teardown_appcontext
def shutdown_session(exception=None):
    db_session.remove()


if __name__ == '__main__':
    app.run(debug=True)
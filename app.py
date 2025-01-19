from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_jwt_extended import JWTManager, create_access_token, jwt_required, get_jwt_identity

app = Flask(__name__)

# Configurations
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
app.config['JWT_SECRET_KEY'] = 'supersecretkey'

db = SQLAlchemy(app)
jwt = JWTManager(app)

# Models
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(100), unique=True, nullable=False)
    password = db.Column(db.String(100), nullable=False)
    role = db.Column(db.String(50), nullable=False)  # 'ops' or 'client'

class File(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    filename = db.Column(db.String(255), nullable=False)
    uploaded_by = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

# API Endpoints
@app.route('/signup', methods=['POST'])
def signup():
    data = request.json
    email = data.get('email')
    password = data.get('password')
    role = data.get('role', 'client')  # Default to client user

    if not email or not password:
        return jsonify({"message": "Email and password are required."}), 400

    if User.query.filter_by(email=email).first():
        return jsonify({"message": "Email already exists."}), 409

    new_user = User(email=email, password=password, role=role)
    db.session.add(new_user)
    db.session.commit()
    return jsonify({"message": "User created successfully."}), 201

if __name__ == '__main__':
    with app.app_context():
        db.create_all()  # Create tables inside the app context
    app.run(debug=True)
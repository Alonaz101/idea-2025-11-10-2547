from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_jwt_extended import JWTManager, jwt_required, create_access_token
import redis

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://localhost/recipesdb'
app.config['JWT_SECRET_KEY'] = 'super-secret-key'

# Initialize extensions
jwt = JWTManager(app)
db = SQLAlchemy(app)

# Redis cache
cache = redis.Redis(host='localhost', port=6379, db=0)

# Models
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password = db.Column(db.String(120), nullable=False)  # store hashed in real

class Mood(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    mood = db.Column(db.String(50), nullable=False)

class Recipe(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200), nullable=False)
    description = db.Column(db.Text)
    mood_tags = db.Column(db.String(200))  # comma-separated

class Favorite(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    recipe_id = db.Column(db.Integer, db.ForeignKey('recipe.id'), nullable=False)

# Routes
@app.route('/login', methods=['POST'])
def login():
    data = request.json
    username = data.get('username')
    password = data.get('password')
    user = User.query.filter_by(username=username, password=password).first()
    if user:
        access_token = create_access_token(identity=user.id)
        return jsonify(access_token=access_token), 200
    return jsonify(msg='Bad username or password'), 401

@app.route('/submit_mood', methods=['POST'])
@jwt_required()
def submit_mood():
    data = request.json
    mood = data.get('mood')
    # Save mood to DB or cache
    return jsonify(msg='Mood submitted', mood=mood), 200

@app.route('/recipes', methods=['GET'])
@jwt_required()
def get_recipes():
    mood = request.args.get('mood')
    # Simple matching via mood_tags
    cached = cache.get(mood)
    if cached:
        return jsonify(recipes=cached.decode('utf-8').split('|'))
    recipes = Recipe.query.filter(Recipe.mood_tags.contains(mood)).all()
    titles = [r.title for r in recipes]
    cache.set(mood, '|'.join(titles), ex=300)
    return jsonify(recipes=titles)

if __name__ == '__main__':
    app.run(debug=True)

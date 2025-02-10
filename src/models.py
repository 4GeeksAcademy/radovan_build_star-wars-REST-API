from flask_sqlalchemy import SQLAlchemy 

db = SQLAlchemy()

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(80), unique=False, nullable=False)
    is_active = db.Column(db.Boolean(), unique=False, nullable=False)

    def __repr__(self):
        return '<User %r>' % self.email

    def serialize(self):
        return {
            "id": self.id,
            "email": self.email,
            # do not serialize the password, its a security breach
        }

# Definición de Planets fuera de la clase User
class Planets(db.Model):
    __tablename__ = 'planets'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(250), nullable=False)
    weather = db.Column(db.String(250))
    population = db.Column(db.Integer)
    
    def to_dict(self):
        return {}

    def __repr__(self):
        return '<Planets %r>' % self.name

    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            "weather": self.weather,
            "population": self.population
        }


class Character(db.Model):
    __tablename__ = 'character'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(250), nullable=False)
    height = db.Column(db.Integer)
    gender = db.Column(db.String(250), nullable=False)
    
    def to_dict(self):
        return {}

    def __repr__(self):
        return '<Character %r>' % self.name

    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            "height": self.height,
            "gender": self.gender
        }

class Favorite(db.Model):
    __tablename__ = 'favorite'
    id = db.Column(db.Integer, primary_key=True)
    planets_id= db.Column(db.Integer, db.ForeignKey('planets.id'))
    planets= db.relationship(Planets)
    
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    user = db.relationship(User)

    character_id = db.Column(db.Integer, db.ForeignKey('character.id'))
    character = db.relationship(Character)

    def to_dict(self):
        return {}

    def __repr__(self):
        return '<Favorite %r>' % self.name

    def serialize(self):
        return {
            "id": self.id,
            "user": self.user.serialize()if self.user != None else "unknown",
            "planets": self.planets.serialize()if self.planets != None else "unknown",
            "character": self.character.serialize()if self.character != None else "unknown",
            
        }
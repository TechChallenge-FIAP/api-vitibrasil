from rest_api.database import db
from passlib.hash import pbkdf2_sha256 as sha256

class User(db.Model):

    __tablename__ = 'user'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(120), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(120), nullable=False)
    
    @classmethod
    def find_by_email(self, email):
        return self.query.filter_by(email=email).first()

    @staticmethod
    def verify_hash(password, hash_):
        return sha256.verify(password, hash_)

    @classmethod
    def all_users(self):
        return self.query.all()

    @staticmethod
    def save(user):
        user.password = sha256.encrypt(user.password)
        db.session.add(user)
        db.session.commit()

    @staticmethod
    def update(user):
        db.session.add(user)
        db.session.commit()
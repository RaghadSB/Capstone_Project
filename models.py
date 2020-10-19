from sqlalchemy import Column, String, create_engine
from flask_sqlalchemy import SQLAlchemy
import json
import os



database_path = os.getenv("DATABASE_URL")

db = SQLAlchemy()

'''
setup_db(app)
    binds a flask application and a SQLAlchemy service
'''


def setup_db(app, database_path=database_path):
    app.config["SQLALCHEMY_DATABASE_URI"] = database_path
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    db.app = app
    db.init_app(app)
    db.create_all()


'''
Person
Have title and release year
'''


class Courses(db.Model):
    __tablename__ = 'Courses'

    id = Column(db.Integer, primary_key=True)
    name = Column(String)
    description = Column(String)
    image_link = Column(String)
    duration = Column(String)
    classes = db.relationship('Classes', backref='class_a', lazy=True)

    def __init__(self, name, description, image_link, duration):
        self.name = name
        self.description = description
        self.image_link = image_link
        self.duration = duration

    def format(self):
        return {
            'id': self.id,
            'name': self.name,
            'description': self.description,
            'image_link': self.image_link,
            'duration': self.duration
        }

    def insert(self):
        db.session.add(self)
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    def update(self):
        db.session.commit()
# --------------------------------------


class Teachers(db.Model):
    __tablename__ = 'Teachers'

    id = Column(db.Integer, primary_key=True)
    name = Column(String)
    email = Column(String)
    image_link = Column(String)
    phone = Column(String)
    profile = Column(String)
    classes = db.relationship('Classes', backref='class_b', lazy=True)

    def __init__(self, name, email, image_link, phone, profile):
        self.name = name
        self.email = email
        self.image_link = image_link
        self.phone = phone
        self.profile = profile

    def format(self):
        return {
            'id': self.id,
            'name': self.name,
            'email': self.email,
            'image_link': self.image_link,
            'phone': self.phone,
            'profile': self.profile
        }

    def insert(self):
        db.session.add(self)
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    def update(self):
        db.session.commit()
# ---------------------------------------


class Classes(db.Model):
    __tablename__ = 'Classes'

    id = Column(db.Integer, primary_key=True)
    name = Column(String)
    start_time = Column(db.DateTime(), nullable=False)
    teacher_id = Column(
        db.Integer,
        db.ForeignKey('Teachers.id'),
        nullable=False)
    course_id = Column(db.Integer, db.ForeignKey('Courses.id'), nullable=False)

    def __init__(self, name, start_time, teacher_id, course_id):
        self.name = name
        self.start_time = start_time
        self.teacher_id = teacher_id
        self.course_id = course_id

    def format(self):
        return {
            'id': self.id,
            'name': self.name,
            'start_time': self.start_time,
            'teacher_id': self.teacher_id,
            'course_id': self.course_id
        }

    def insert(self):
        db.session.add(self)
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    def update(self):
        db.session.commit()

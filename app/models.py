# app/models.py
from flask_mongoengine import MongoEngine

db = MongoEngine()

class Course(db.Document):
    course_name = db.StringField(required=True)
    course_code = db.StringField(unique=True, required=True)
    course_duration = db.IntField(required=True)

class Student(db.Document):
    name = db.StringField(required=True)
    course_id = db.ReferenceField(Course)

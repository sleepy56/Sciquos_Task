# app/routes.py
from flask import Flask, request, jsonify
from app.models import db, Course, Student

@app.route('/add_course', methods=['POST'])
def add_course():
    data = request.json
    course = Course(**data)
    course.save()
    return jsonify({"message": "Course added successfully"})

# Implement other routes following the specified requirements

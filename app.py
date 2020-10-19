import os
from flask import (Flask, render_template, request, Response,
                   redirect, url_for, jsonify, abort)
import json
from flask_sqlalchemy import SQLAlchemy
import logging
from logging import Formatter, FileHandler
import sys
from flask_cors import CORS, cross_origin
from flask_migrate import Migrate
from models import setup_db, Teachers, Courses, Classes
from auth import AuthError, requires_auth

# ---------------------------------------------------------


def create_app(test_config=None):
    app = Flask(__name__)
    setup_db(app)
    # CORS(app)
    cors = CORS(app, resources={r"/api/*": {"origins": "*"}})

    @app.after_request
    def after_request(response):
        response.headers.add(
            'Access-Control-Allow-Headers',
            'Content-Type,Authorization')
        response.headers.add('Access-Control-Allow-Credentials', 'true')
        response.headers.add(
            'Access-Control-Allow-Methods',
            'GET,PATCH,POST,DELETE,OPTIONS')
        return response

    @app.route('/Teachers')
    def get_teachers():
        data = Teachers.query.all()
        dataforma = [d.format() for d in data]
        return jsonify({"success": True, "teachers": dataforma})
# ***********************************************************

    @app.route('/Classes')
    def get_Classes():
        data = Classes.query.all()
        dataforma = [d.format() for d in data]
        return jsonify({"success": True, "Classes": dataforma})
# ***********************************************************

    @app.route('/Courses')
    def get_Courses():
        data = Courses.query.all()
        dataforma = [d.format() for d in data]
        return jsonify({"success": True, "Courses": dataforma})
# **********************************************************

    @app.route('/Courses', methods=['POST'])
    @requires_auth('post:courses')
    def add_Courses(payload):
        name = request.get_json()['name']
        description = request.get_json()['description']
        image_link = 'https://www.freeiconspng.com/thumbs/'\
            + 'book-icon/book-icon-black-good-galleries--24.jpg'
    #  request.get_json()['image_link']
        duration = request.get_json()['duration']
        try:
            course = Courses(
                name=name,
                description=description,
                image_link=image_link,
                duration=duration)
            course.insert()

            return jsonify({"success": True, "Courses": course.format()})
        except BaseException:
            abort(422)
# ---------------------------------------------------------

    @app.route('/Teachers', methods=['POST'])
    @requires_auth('post:teachers')
    def add_Teachers(payload):
        name = request.get_json()['name']
        email = request.get_json()['email']
        image_link = 'https://www.iconfinder.com/data/'\
            + 'icons/men-avatars-icons-set-1/256/21-512.png'
    #  request.get_json()['image_link']
        phone = request.get_json()['phone']
        profile = request.get_json()['profile']
        try:
            teacher = Teachers(
                name=name,
                email=email,
                image_link=image_link,
                phone=phone,
                profile=profile)
            teacher.insert()

            return jsonify({"success": True, "Teachers": teacher.format()})
        except BaseException:
            abort(422)
# -----------------------------------------------------------

    @app.route('/Classes', methods=['POST'])
    @requires_auth('post:classes')
    def create_class(payload):
        name = request.get_json()['name']
        start_time = request.get_json()['start_time']
        teacher_id = request.get_json()['teacher_id']
        course_id = request.get_json()['course_id']
        try:
            claass = Classes(
                name=name,
                start_time=start_time,
                teacher_id=teacher_id,
                course_id=course_id)
            claass.insert()

            return jsonify({"success": True, "Courses": claass.format()})
        except BaseException:
            abort(422)
# -----------------------------------------------------------

    @app.route('/Classes/<int:class_id>', methods=['PATCH'])
    @requires_auth('patch:classes')
    def edit_class(payload, class_id):
        all_classes = Classes.query.all()
        flag = False
        for da in all_classes:
            if class_id == da.id:
                flag = True
        if not flag:
            abort(404)
        if flag:
            try:
                data = request.get_json()
                theclass = Classes.query.get(class_id)
                if'name' in data:
                    theclass.name = request.get_json()['name']
                if 'start_time' in data:
                    theclass.start_time = request.get_json()['start_time']
                if 'teacher_id' in data:
                    theclass.teacher_id = request.get_json()['teacher_id']
                if 'course_id' in data:
                    theclass.course_id = request.get_json()['course_id']
                theclass.update()
                return jsonify({"success": True, "edit": class_id})
            except BaseException:
                abort(422)
# -----------------------------------------------------------------

    @app.route('/Classes/<int:class_id>', methods=['DELETE'])
    @requires_auth('delete:classes')
    def delete_class(payload, class_id):
        all_classes = Classes.query.all()
        flag = False
        for da in all_classes:
            if class_id == da.id:
                flag = True
        if not flag:
            abort(404)
        if flag:
            try:
                theclass = Classes.query.get(class_id)
                theclass.delete()
                return jsonify({"success": True, "delete": class_id})
            except BaseException:
                abort(422)
# --------------------------------------------------------------

    @app.errorhandler(422)
    def unprocessable(error):
        return jsonify({
            "success": False,
            "error": 422,
            "message": "unprocessable"
        }), 422

    @app.errorhandler(403)
    def Forbidden(error):
        return jsonify({
            "success": False,
            "error": 403,
            "message": "Access is forbidden to the requested page."
        }), 403

    @app.errorhandler(500)
    def InternalError(error):
        return jsonify({
            "success": False,
            "error": 500,
            "message": "Internal Server Error."
        }), 500

    @app.errorhandler(400)
    def BadRequest(error):
        return jsonify({
            "success": False,
            "error": 400,
            "message": "Bad Request."
        }), 400

    @app.errorhandler(404)
    def NotFound(error):
        return jsonify({
            "success": False,
            "error": 404,
            "message": "Not Found."
        }), 404

    @app.errorhandler(AuthError)
    def handle_auth_error(ex):
        response = jsonify(ex.error)
        response.status_code = ex.status_code
        return response

    return app


app = create_app()

if __name__ == '__main__':
    app.run()

from . import auth_blueprint

from flask.views import MethodView
from flask import Blueprint, make_response, request, jsonify
from app.models import User


class RegistrationView(MethodView):
    """This class registers a new user."""

    def post(self):
        user = User.query.filter_by(email=request.data['email']).first()

        if not user:
            try:
                post_data = request.data
                # Register the user
                email = post_data['email']
                password = post_data['password']
                user = User(email=email, password=password)
                user.save()

                response = {
                    'message': 'You registered successfully.',
                    'info': 'Please log in to get access.'
                }
                return make_response(jsonify(response)), 201
            except Exception as e:
                response = {
                    'message': str(e)
                }
                return make_response(jsonify(response)), 401
        else:
            response = {
                'message': 'User already exists. Please log in.'
            }

            return make_response(jsonify(response)), 202


registration_view = RegistrationView.as_view('register_view')
auth_blueprint.add_url_rule(
    '/auth/register',
    view_func=registration_view,
    methods=['POST'])

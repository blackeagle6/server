from flask.views import MethodView
from flask import Blueprint, request

users_blueprint = Blueprint("users_blueprint", __name__, url_prefix='/api/')

class UsersList(MethodView):
    def get(self):

        return [{ "name": "Jose" }, { "name": "Ricardo"}]

class Users(MethodView):
    def post(self):
        data = request.get_json()

        email = data.get('email')
        username = data.get('username')

        if email is None:
            return { "message": "No has ingresado tu correo."}
users_blueprint.add_url_rule(
    'users',
    view_func=UsersList.as_view("users_list")
)

users_blueprint.add_url_rule(
    'users',
    view_func=Users.as_view("users")
)
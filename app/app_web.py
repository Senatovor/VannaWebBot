from vanna.flask.auth import AuthInterface
import flask
import os
from vanna.flask import VannaFlaskApp
from vanna_setup import vn
from config import settings


class SimplePassword(AuthInterface):
    def __init__(self, users: dict):
        self.users = users

    def get_user(self, flask_request) -> any:
        return flask_request.cookies.get('user')

    def is_logged_in(self, user: any) -> bool:
        return user is not None

    def override_config_for_user(self, user: any, config: dict) -> dict:
        return config

    def login_form(self) -> str:
        with open(
                os.path.join(os.path.dirname(__file__), '..', 'templates', 'login_form.html'),
                "r",
                encoding="utf-8"
        ) as file:
            html_string = file.read()
        return html_string

    def login_handler(self, flask_request):
        email = flask_request.form['email']
        password = flask_request.form['password']
        # Find the user and password in the users dict
        for user in self.users:
            if user["email"] == email and user["password"] == password:
                response = flask.make_response('Logged in as ' + email)
                response.set_cookie('user', email)
                # Redirect to the main page
                response.headers['Location'] = '/'
                response.status_code = 302
                return response
        else:
            return 'Login failed'

    def callback_handler(self, flask_request):
        user = flask_request.args['user']
        response = flask.make_response('Logged in as ' + user)
        response.set_cookie('user', user)
        return response

    def logout_handler(self, flask_request):
        response = flask.redirect('/login')
        response.delete_cookie('user')
        return response


if __name__ == '__main__':
    VannaFlaskApp(
            vn=vn,
            auth=SimplePassword(users=settings.get_users()),
            allow_llm_to_see_data=True,
            title="Приветствуем!",
            subtitle="Это тестовый бот",
            show_training_data=True,
            sql=True,
            table=True,
            chart=True,
            summarization=False,
            ask_results_correct=True,
    ).run(host='0.0.0.0', port=5000, debug=True)

from flask import render_template, Blueprint

users_blueprint = Blueprint('users', __name__, template_folder='templates')

@users_blueprint.route('/login')
def login():
    return render_template('login.html')
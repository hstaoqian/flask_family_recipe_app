from flask import render_template, Blueprint

recipes_blueprint = Blueprint('recipes', __name__, template_folder='templates')

@recipes_blueprint.route('/')
def index():
    return render_template('index.html')
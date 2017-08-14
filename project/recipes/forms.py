from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms.validators import DataRequired


class AddRecipeForm(FlaskForm):
    recipe_title = StringField('Recipe Title', validators=[DataRequired()])
    recipe_description = StringField('Recipe Description', validators=[DataRequired()])
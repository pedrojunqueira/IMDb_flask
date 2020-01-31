from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField
from wtforms.validators import DataRequired


class ReviewForm(FlaskForm):
    content = TextAreaField('Review', validators=[DataRequired()])
    submit = SubmitField('Predict')


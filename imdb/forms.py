from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField, RadioField
from wtforms.validators import DataRequired


class ReviewForm(FlaskForm):
    content = TextAreaField('Review', validators=[DataRequired()])
    label = RadioField('Label', validators=[DataRequired()], choices=[
                       ('positive', 'positive'), ('negative', 'negative')])
    submit = SubmitField('Predict')


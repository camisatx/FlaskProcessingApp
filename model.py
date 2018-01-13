from flask_wtf import FlaskForm
from wtforms import FloatField, validators


class ProcessForm(FlaskForm):

    data_field = FloatField(
        label='Data Field',
        validators=[validators.Optional()],
    )

from flask_wtf import FlaskForm
from wtforms import IntegerField, SelectField, StringField, SubmitField
from wtforms.validators import DataRequired


class MainForm(FlaskForm):
    quantity = IntegerField(
        "Quantity",
        validators=[DataRequired()],
        render_kw={"value": "1"},
    )
    prefix = SelectField(
        "Prefix",
        choices=[
            ("", "None"),
            ("+62", "[+62]"),
            ("62", "[62]"),
            ("0", "[0]"),
        ],
    )
    duplication = SelectField(
        "Duplication",
        choices=[
            ("0.0", "0%"),
            ("0.1", "10%"),
            ("0.2", "20%"),
            ("0.3", "30%"),
            ("0.4", "40%"),
            ("0.5", "50%"),
        ],
    )
    header = StringField(
        "Header",
        validators=[DataRequired()],
        render_kw={"placeholder": "Enter text here"},
    )
    submit = SubmitField("Generate")

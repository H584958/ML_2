from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, BooleanField, SubmitField, FloatField
from wtforms.validators import DataRequired, NumberRange

class DataForm(FlaskForm):
    budget = FloatField('Budget')

    popularity = FloatField('Popularity')

    runtime = FloatField('Runtime')

    has_collection = IntegerField('Collection. 1=Has a collection 0=No collection', validators=[NumberRange(min=0, max=1)])

    has_homepage = IntegerField('Homepage. 1=Has a homepage 0=No homepage', validators=[NumberRange(min=0, max=1)])

    is_en_original_language = IntegerField('Original language. 1=english 0=No english', validators=[NumberRange(min=0, max=1)])

    collection_and_homepage = IntegerField('Collection and homepage. 1=has a collection and homepage 0=No homepage or collection', validators=[NumberRange(min=0, max=1)])

    produced_US = IntegerField('Produced in. 1=produced in US 0=another country', validators=[NumberRange(min=0, max=1)])

    crew_count = IntegerField('How many in crew. min 1 and max 10000 ', validators=[NumberRange(min=1, max=10000)])

    cast_count = IntegerField('How many in cast. min 1 and max 10000 ', validators=[NumberRange(min=1, max=10000)])

    submit = SubmitField('Submit')
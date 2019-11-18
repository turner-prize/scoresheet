from config import ma,db
from models import Scores

class ScoresSchema(ma.ModelSchema):
    class Meta:
        model = Scores
        sqla_session = db.session
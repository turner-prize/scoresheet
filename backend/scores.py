from config import db
from models import Scores
from schemas import ScoresSchema
from datetime import date

def read_all():
    d = Scores.query.all()
    scores_schema = ScoresSchema(many=True)
    return scores_schema.dump(d).data
    
def assignPoints(name,scores):
    if scores['winner'] == name:
        x = 3
    elif scores['runnerup'] == name:
        x= 1
    else:
        x= 0
    return x
    
def create(scores):
    gameDate=date.today()
    Will= assignPoints('Will',scores)
    Dan= assignPoints('Dan',scores)
    Ben= assignPoints('Ben',scores)
    Sven= assignPoints('Sven',scores)
    
    print(gameDate)

    existing_record = None

    # Can we insert this person?
    if existing_record is None:

        # Create a person instance using the schema and the passed-in person
        schema = ScoresSchema()
        new_record = schema.load(scores, session=db.session).data

        # Add the person to the database
        
        newScores = Scores(gameDate=gameDate,Will=Will,Dan=Dan,Ben=Ben,Sven=Sven)
        
        db.session.add(newScores)
        db.session.commit()

        # Serialize and return the newly created person in the response
        return schema.dump(new_record).data, 201

    # Otherwise, nope, person exists already
    else:
        abort(409, f'Record exists already')
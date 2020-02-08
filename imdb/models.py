from imdb import db
from datetime import datetime



class Review(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    body = db.Column(db.String(500))
    prediction = db.Column(db.String(20))
    probability = db.Column(db.Float())
    label = db.Column(db.String(20))
    timestamp = db.Column(db.DateTime, index=True, default=datetime.utcnow)
    

    def __repr__(self):
        return '<Post {}>'.format(self.body)

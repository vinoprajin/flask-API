
from app import db

class ToDo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    description = db.Column(db.String(200), nullable=False)

    def __repr__(self):
        return f"ToDo('{self.description}')"

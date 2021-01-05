"""Models for Cupcake app."""
from flask_sqlalchemy import SQLAlchemy

DEFAULT_IMAGE = "https://tinyurl.com/demo-cupcake"

db = SQLAlchemy()

def connect_db(app):
    db.app = app
    db.init_app(app)

# Models
class Cupcake(db.Model):
    """ Cupcake Model """
    __tablename__ = "cupcakes"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    flavor = db.Column(db.Text, nullable=False)
    size = db.Column(db.Text, nullable=False)
    rating = db.Column(db.Float, nullable=False)
    image = db.Column(db.Text, default=DEFAULT_IMAGE)

    def image_url(self):
        """ Return image or default image """ 
        return self.image or DEFAULT_IMAGE

    def serialize(self):
        """ Returns a dict representation of a cupcake which we can turn into JSON """
        return {
          'id': self.id,
          'flavor': self.flavor,
          'size': self.size,
          'rating': self.rating,
          'image': self.image
        }

    def __repr__(self):
        return f"<Cupcake: (flavor:'{self.flavor}, size: '{self.size}, rating: '{self.rating}') >"
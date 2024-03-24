from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class News(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String, nullable=False)
    url = db.Column(db.String, unique=True, nullable=False)
    img_icon = db.Column(db.String, unique=True, nullable=False)
    published = db.Column(db.DateTime, nullable=False)

    def __repr__(self):
        return '<News {} {}>'.format(self.title, self.url)
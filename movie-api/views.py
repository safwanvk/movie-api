from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

db = SQLAlchemy(app)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'


class Movie(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(50))
    rating = db.Column(db.Integer)


db.create_all()


@app.route('/add_movie', methods=['POST'])
def add_movie():
    movie_data = request.get_json()
    new_movie = Movie(title=movie_data['title'], rating=movie_data['rating'])

    db.session.add(new_movie)
    db.session.commit()

    return 'Done', 201


@app.route('/get_movie', methods=['GET'])
def get_movie():
    movie_list = Movie.query.all()
    movies = []
    for movie in movie_list:
        movies.append({'title': movie.title, 'rating': movie.rating})

    return jsonify({'moves': movies})


if __name__ == '__main__':
    app.run(debug=True)

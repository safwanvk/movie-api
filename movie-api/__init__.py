from flask import Flask

app = Flask(__name__)

app.config['SQLAlchemy_DATABASE_URI'] = 'sqlite///database.db'

if __name__ == '__main__':
    app.run(debug=True)

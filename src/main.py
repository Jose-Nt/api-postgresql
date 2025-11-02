from api.routes import routes
from flask import Flask

app = Flask(__name__)
app.register_blueprint(routes)

if __name__ == '__main__':
    app.run(port=5000, host='localhost', debug=True)
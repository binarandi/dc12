import os

from flask import Flask, render_template
#from flask_restful import Resource, Api
from models import *

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = os.getenv("DATABASE_URL")
#api = Api(app)
db.init_app(app)

@app.route("/")
def index():
    things = Thing.query.all()
    return render_template("index.html", things=things)

#def main:
    #db.create_all()

#class App(Resource):
    #def get(self):
        #return {
            #'db': ['1', '2', '3','Eggs']
        #}

#api.add_resource(App, '/')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80, debug=True)

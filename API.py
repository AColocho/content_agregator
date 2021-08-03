from flask import Flask
from flask_restful import Resource, Api
from scrape import ESPN

app = Flask(__name__)
api = Api(app)

class ESPN_API(Resource):
    def get(self):
        data = ESPN().get_top_news()
        return {'espn': data}

api.add_resource(ESPN_API, '/espn')

if __name__ == '__main__':
    app.run(debug=False)
from flask import Flask, request
from flask_cors import CORS, cross_origin
import database_queries

app = Flask(__name__)
cors = CORS(app)
# app.config['CORS_HEADERS'] = 'Content-Type'


@app.route("/")
@cross_origin()
def helloWorld():
  return {'response': 'App is up!'}


@app.route("/getallfoods")
@cross_origin()
def get_all_foods():
  return {'response': database_queries.get_all_foods()}


@app.route("/addnewfood", methods=['POST'])
@cross_origin()
def add_new_food():
    request_data = request.get_json()
    print(request_data)
    if database_queries.add_new_food(request_data['name'], request_data['rating'], request_data['restaurant'], request_data['category'], request_data['min_price_range'], request_data['max_price_range'], request_data['nationality']) > 0:
        return "Success!"
    return "Something went wrong!"

if __name__ == '__main__':
    app.run(debug=True)
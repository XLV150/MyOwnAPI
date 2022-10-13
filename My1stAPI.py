import random
from flask import *
import json, time
import pandas
import pandas as pd
import copy

app = Flask(__name__)

# def random_car_func():
#     random_car = random.randint(0, 400)
#
#     data_csv = pd.read_csv("Cars.csv", sep=';')
#     random_car_str = data_csv.iloc[random_car]
#     return random_car_str

@app.route('/', methods=['GET'])
def home_page():
    random_car = random.randint(0, 406)

    data_csv = pd.read_csv("Cars.csv", sep=';')
    random_car_str = data_csv.iloc[random_car]

    data_set = {'car': {'name': f'{random_car_str["Car"]}'},
                'mpg': f'{random_car_str["MPG"]}',
                'cylinders': f'{random_car_str["Cylinders"]}',
                'displacement': f'{random_car_str["Displacement"]}',
                'horsepower': f'{random_car_str["Horsepower"]}',
                'weight': f'{random_car_str["Weight"]}',
                'acceleration': f'{random_car_str["Acceleration"]}',
                'model': f'{random_car_str["Model"]}',
                'origin': f'{random_car_str["Origin"]}'}

    json_dump = json.dumps(data_set)

    return json_dump


@app.route('/car/', methods=['GET'])
def request_page():

    data_csv = pd.read_csv("Cars.csv", sep=';')
    user_query = request.args.get('car_no')
    user_query = int(user_query)
    chosen1 = data_csv.iloc[user_query]

    data_set = {'car': {'name': f'{chosen1["Car"]}'},
                'mpg': f'{chosen1["MPG"]}',
                'cylinders': f'{chosen1["Cylinders"]}',
                'displacement': f'{chosen1["Displacement"]}',
                'horsepower': f'{chosen1["Horsepower"]}',
                'weight': f'{chosen1["Weight"]}',
                'acceleration': f'{chosen1["Acceleration"]}',
                'model': f'{chosen1["Model"]}',
                'origin': f'{chosen1["Origin"]}'}

    json_dump = json.dumps(data_set)
    return json_dump

if __name__ == __name__:
    app.run()

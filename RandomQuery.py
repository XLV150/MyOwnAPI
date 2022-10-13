import requests

url = 'http://127.0.0.1:7777' #/car/?car_no=

response = requests.request('GET', url)

print(response)
print(response.text)
print()

data = response.json()

if response.status_code == 200:
    car = data['car']['name']
    mpg = data['mpg']
    cylinders = data['cylinders']
    displacement = data['displacement']
    horsepower = data['horsepower']
    weight = data['weight']
    acceleration = data['acceleration']
    model = data['model']
    origin = data['origin']

    print("Car name:", car)
    print("Miles per gallon:", mpg)
    print("Cylinders:", cylinders)
    print("Engine Displacement:", displacement)
    print("Horsepower:", horsepower)
    print("Weight:", weight)
    print("Acceleration:", acceleration)
    print("Model:", model)
    print("Origin:", origin)
else:
    print("Unable to retrieve data. Code: ", response)
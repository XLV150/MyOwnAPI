import requests

user_query = input('Enter a number 1- 406: ')

url = f'http://127.0.0.1:7777/car/?car_no={user_query}'

response = requests.request('GET', url)

print(response)
print(response.text)
print()

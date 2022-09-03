import requests

resp = requests.get('http://127.0.0.1:8000/', headers={'hello': 'Worlaaad'})

user_agent = {'user_agent': 'My User Agent 1.0'}
resp = requests.get('http://127.0.0.1:8000/', headers = user_agent)
print(resp.content)
print(resp.headers)

resp = requests.post('http://127.0.0.1:8000/users', json={"name":"Dante", "age":"20"})
resp.content

#
resp = requests.post('http://127.0.0.1:8000/users/POL', json={"name":"Dante", "age":20})
resp.content

#Post
resp = requests.post('http://127.0.0.1:8000/posts', json={"title":'Doctor'})
resp.content

# to fetch data as form
resp = requests.post('http://127.0.0.1:8000/users/LUX', data={"name":"Dante", "age":20})
resp.content

files = {'file': open(r'C:/Users/LENOVO/Desktop/projects_web/assets/cat.jpg','rb')}

resp = requests.post('http://127.0.0.1:8000/files',files=files)
resp.content

# custom headers
resp = requests.get('http://127.0.0.1:8000/')
resp.headers

#Post password
resp = requests.post('http://127.0.0.1:8000/password', json={"password":'123', 'password_confirm':'15'})
resp.content
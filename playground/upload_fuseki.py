import requests

# x = requests.get('http://fuseki:3030/fill-kg/')
# print(x.text)

data = open('fill-kg-nt.txt').read()
headers = {'Content-Type': 'text/turtle;charset=utf-8'}
r = requests.post('http://fuseki:3030/fill-kg/data?default', data=data, headers=headers)

print(r.text)
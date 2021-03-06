import requests
# pip3 install requests

key = 'VAS_KLUC_PRE_IFTTT'
url = 'https://maker.ifttt.com/trigger/pocasie/with/key/{key}'

data = {
    "value1":"20.5",
    "value2":"44"
}

headers = {
    'Content-Type': 'application/json'
}

response = requests.post(
    url.format(key=key),
    headers=headers,
    json=data
)
print(response)

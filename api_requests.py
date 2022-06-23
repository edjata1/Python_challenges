# when using import request in terminal: pip install requests
import requests
response = requests.get("http://randomfox.ca/floof")
fox = response.json()
print(fox['image'])
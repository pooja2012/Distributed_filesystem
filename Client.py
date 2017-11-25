import json
import requests as req
url="http://0.0.0.0:8080/"

filepath=raw_input("Enter the file name:")
file=url+filepath
response=req.get(url)
print("Response",response.text)

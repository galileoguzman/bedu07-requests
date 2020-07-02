import requests
import csv

response = requests.get('http://api.github.com/')

# print(response)
# Print status code
# print(response.content)

print(response.status_code)
print(response.text) # transform in dict

csv.writer(dict)

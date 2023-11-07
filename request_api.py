import requests

url = "http://localhost:9797/predict"

#data exemple to send to api flask 
employee = { 
 "Education":  "0",
 "JoiningYear": "2013",
 "City": "Pune",
 "PaymentTier": "1",
 "Age": "28",
 "Gender": "0",
 "EverBenched": "0",
 "ExperienceInCurrentDomain": "3"
 }

print("\n`Exemple employee (you can modify file request_api.py for change data) : \n", employee)

response = requests.post(url, json=employee).json()

print(response)



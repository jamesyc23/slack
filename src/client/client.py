import requests

payload = {'name': 'wuisawesome'}
r = requests.get('http://localhost:5000', params=payload)
print(r.text)

# Function polling for new messages
# Notifications

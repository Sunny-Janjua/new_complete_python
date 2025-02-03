import requests

# API URL
url = "https://api.freeapi.app/api/v1/public/randomusers"

# Fetch data from API
response = requests.get(url)

# Convert response to JSON
newResponse = response.json()

# Extract data
data = newResponse.get("data", {})  # Get 'data' safely

# Check if 'data' contains a list
if isinstance(data.get("data"), list):
    users = data["data"]  # Extract user list
    
    # Print names of users
    for user in users:
        print(f"Name: {user.get('name', 'No Name Found')}")  # Use .get() to avoid KeyError
else:
    print("Invalid data structure received from API")

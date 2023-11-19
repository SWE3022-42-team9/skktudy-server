import time

import requests

# Set the base URL for the Flask server
base_url = "http://127.0.0.1:5000"

# Define the API endpoint to send a GET request to
api_endpoint = "/chatbot/log"


# Record the start time
start_time = time.time()

data = {
    "uid": 0,
    "message": "OS가 뭘까?",
}

response = requests.post(base_url + api_endpoint, json=data)

# Record the end time
end_time = time.time()

# Calculate the time taken for the request
elapsed_time = end_time - start_time

# Check if the request was successful (status code 200)
if response.status_code == 200:
    print(response.text)
    print(f"Request took {elapsed_time:.2f} seconds to complete.")
else:
    print(f"Request failed with status code: {response.status_code}")

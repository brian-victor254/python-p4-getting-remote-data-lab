import requests
import json

class GetRequester:

    def __init__(self, url):
        self.url = url

    def get_response_body(self):
        # Send a GET request to the URL and return the response body as text
        response = requests.get(self.url)
        return response.text

    def load_json(self):
        # Use get_response_body to get the response body and convert it to JSON
        response_body = self.get_response_body()
        return json.loads(response_body)

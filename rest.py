import requests
import jwt

class Rest:

    __token = None

    def get_bearer_token(self, grant_type, client_id, client_secret, username, password, token_url):
        data = {
            'grant_type': grant_type,
            'client_id': client_id,
            'client_secret': client_secret,
            'username': username,
            'password': password            
        }
        response = requests.post(token_url, data=data)
        if response.status_code == 200:
            self.__token = response.json().get('access_token')
            return self.__token

    def execute_get(self):
        url = "https://example.com/api"
        headers = {"Content-Type": "application/json"}

        response = requests.get(url, headers=headers)
        
        if response.status_code == 200:
            print("GET request successful.")
        else:
            print(f"GET request failed with status code {response.status_code}.")

    def execute_post(self):
        url = "https://example.com/api"
        data = {"key": "value"}
        headers = {
            "Content-Type": "application/json",
            "Authorization": "Bearer YOUR_ACCESS_TOKEN"
        }

        response = requests.post(url, json=data, headers=headers)
        
        if response.status_code == 200:
            print("POST request successful.")
        else:
            print(f"POST request failed with status code {response.status_code}.")

    def execute_put(self):
        url = "https://example.com/api"
        data = {"key": "value"}
        headers = {"Content-Type": "application/json"}

        response = requests.put(url, json=data, headers=headers)
        
        if response.status_code == 200:
            print("PUT request successful.")
        else:
            print(f"PUT request failed with status code {response.status_code}.")

    def execute_delete(self):
        url = "https://example.com/api"
        headers = {"Content-Type": "application/json"}

        response = requests.delete(url, headers=headers)
        
        if response.status_code == 200:
            print("DELETE request successful.")
        else:
            print(f"DELETE request failed with status code {response.status_code}.")

    def execute_patch(self):
        url = "https://example.com/api"
        data = {"key": "value"}
        headers = {"Content-Type": "application/json"}

        response = requests.patch(url, json=data, headers=headers)
        
        if response.status_code == 200:
            print("PATCH request successful.")
        else:
            print(f"PATCH request failed with status code {response.status_code}.")


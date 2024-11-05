import requests

class PersistentEntity:
    def __init__(self) -> None:
        self.changes = {}

    def __setattr__(self, name, value):
        self.changes[name] = value
        super().__setattr__(name, value)

    def __execute_get(self):
        url = "https://example.com/api"
        headers = {"Content-Type": "application/json"}

        response = requests.get(url, headers=headers)
        
        if response.status_code == 200:
            print("GET request successful.")
        else:
            print(f"GET request failed with status code {response.status_code}.")

    def __execute_post(self):
        url = "https://example.com/api"
        data = {"key": "value"}
        headers = {"Content-Type": "application/json"}

        response = requests.post(url, json=data, headers=headers)
        
        if response.status_code == 200:
            print("POST request successful.")
        else:
            print(f"POST request failed with status code {response.status_code}.")

    def __execute_put(self):
        url = "https://example.com/api"
        data = {"key": "value"}
        headers = {"Content-Type": "application/json"}

        response = requests.put(url, json=data, headers=headers)
        
        if response.status_code == 200:
            print("PUT request successful.")
        else:
            print(f"PUT request failed with status code {response.status_code}.")

    def __execute_delete(self):
        url = "https://example.com/api"
        headers = {"Content-Type": "application/json"}

        response = requests.delete(url, headers=headers)
        
        if response.status_code == 200:
            print("DELETE request successful.")
        else:
            print(f"DELETE request failed with status code {response.status_code}.")

    def __execute_patch(self):
        url = "https://example.com/api"
        data = {"key": "value"}
        headers = {"Content-Type": "application/json"}

        response = requests.patch(url, json=data, headers=headers)
        
        if response.status_code == 200:
            print("PATCH request successful.")
        else:
            print(f"PATCH request failed with status code {response.status_code}.")

    def insert(self) -> None:
        self.__execute_post()



# Usage
entity = PersistentEntity()
entity.insert()
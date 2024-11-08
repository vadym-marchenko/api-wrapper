import requests


class PersistentEntity:
    def __init__(self) -> None:
        self.changes = {}

    def __setattr__(self, name, value):
        self.changes[name] = value
        super().__setattr__(name, value)



    def insert(self) -> None:
        self.__execute_post()




# Usage
entity = PersistentEntity()
entity.insert()
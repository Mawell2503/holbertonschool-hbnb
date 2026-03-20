#  a tool to create unique IDs for my project
import uuid
#  a tool to keep track of when things are done
from datetime import datetime

class BaseModel:
    def __init__(self):
        #  generates a unique ID
        self.id = str(uuid.uuid4())
        #  set creation timestamp
        self.created_at = datetime.now()
        #  set last updated timestamps
        self.update_at = datetime.now()

    def save(self):
        self.update_at = datetime.now()

    def update(self, data):
        for key, value in data.items():
            if hasattr(self, key):
                setattr(self, key, value)
        self.save()
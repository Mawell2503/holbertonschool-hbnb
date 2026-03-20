from app.models.BaseModel import BaseModel

class Amenity(BaseModel):
    def __init__(self, name):
        super().__init__()

        if len(name) > 50:
            raise ValueError("max character for amenity is 50")
        
        self.name = name
    
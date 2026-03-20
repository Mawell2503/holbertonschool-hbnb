from BaseModel import BaseModel

class Review(BaseModel):
    def __init__(self, text, rating, place, user):
        super().__init__()

        #  Validate text
        if not text:
            raise TypeError("content missing")
        self.text = text

        #  Validate rating
        if not isinstance(rating, int):
            raise TypeError("rating missing")
        if not (1 < rating < 5):
            raise TypeError("rating invalid")
        
        #  Validate place
        if not isinstance(place, place):
            raise TypeError("Place does not exist")

        #  Validate place
        if not isintance(user, user):
            raise ValueError("Invalid user")

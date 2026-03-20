from BaseModel import BaseModel

class Place(BaseModel):
    def __init__(self, title, description, price, latitude, longitude, owner):
        super().__init__()

        self.reviews = []
        self.amenities = []

        #  Validate title
        if not isinstance(title, str):
            raise ValueError("No title")
        if len(title) > 100:
            raise ValueError("Character limit is 100")
        self.title = title
        
        #  Validate description
        if not isinstance(description, str):
            raise ValueError("Description incorrect")
        self.description = description
        
        #  Validate price
        if not isinstance(price, float):
            raise ValueError("Price is required")
        if price <= 0:
            raise ValueError("Price doesnt exist")
        self.price = price
        
        #  Validate latitude
        if not isinstance(latitude, float):
            raise ValueError("Latitude required")
        if not (-90.0 < latitude < 90.0):
            raise ValueError("Coordinates incorrect")
        self.latitude = latitude
        
        #  Validate longitude
        if not isinstance(longitude, float):
            raise TypeError("Longitude required")
        if not (-180.0 < longitude < 180.0):
            raise ValueError("Coordinates incorrect")
        self.longitude = longitude

        #  Validate owner
        if not owner:
            raise ValueError("Owner must be provided")
        self.owner = owner

        def add_review(self, review):
            if not isinstance(review, Review):
                raise TypeError("Review missing")
            self.reviews.append(review)

        def add_amenity(self, amenity):
            if not isinstance(amenity, Amenity):
                raise TypeError("Amenity missing")
            self.amenities.append(amenity)

        BaseModel.update()

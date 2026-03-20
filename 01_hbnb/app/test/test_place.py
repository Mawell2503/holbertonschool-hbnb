from app.models.place import Place
from app.models.user import User
from app.models.review import Review

def test_place_creation(self):
    owner = User(first_name="Alice", last_name="smith", email= "alice.smith@example.com")
    place = Place(title="cozy apartment", description="A nice place to say", price=100, latitude=37.7749, longitude=-122.4)

    review = Review (text="Great stay!", rating=5, place=place, user=owner)
    place.add_review(review)

    assert place.title == "cozy apartment"
    assert place.price == 100
    assert len(place.reviews) == 1
    assert place.reviews[0].text == "Great stay!"

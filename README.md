# holbertonschool-hbnb

## Layers
    layers speaks in an order(top -> middle -> bottom)
    # Presentation Layer(Top layer)
    # Business Logic Layer (Middle layer)
    # Persistence/Data Layer (Bottom layer)

# Projects and files

# Directory and files
hbnb/
├── app/ 
│   ├── __init__.py                     # initialize flask app
│   ├── api/                            # contains API endpoint
│   │   ├── __init__.py
│   │   ├── v1/                         # first version of API
│   │       ├── __init__.py
                                        # endpoints
│   │       ├── users.py
│   │       ├── places.py
│   │       ├── reviews.py
│   │       ├── amenities.py
│   ├── models/                         # defines application data models
│   │   ├── __init__.py
                                        # models
│   │   ├── user.py
│   │   ├── place.py
│   │   ├── review.py
│   │   ├── amenity.py
│   ├── services/                       # application services
│   │   ├── __init__.py
│   │   ├── facade.py                   # communicates between layers
│   ├── persistence/                    # data persistence layer
│       ├── __init__.py
│       ├── repository.py               #repository for database
├── run.py                              # runs application
├── config.py                           # configurations
├── requirements.txt                    # project requirements
├── README.md                           # documentation
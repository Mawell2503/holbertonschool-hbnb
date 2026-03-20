from BaseModel import BaseModel

class User(BaseModel):

    def __init__(self, first_name, last_name, email, role="user"):
        #  calls the __init__ function in Basemodel.
        #  creates id for each user
        #  creates a timestamps for when each user was created...
        #  ...and when modification was made
        super().__init__()

        #  Validate & assign first_name
        if not isinstance(first_name, str):
            raise ValueError("First name is required")
        if len(first_name) > 50:
            raise ValueError("Character limit is 50")
        self.first_name = first_name
        
        #  Validate & assign last_name
        if not isinstance(last_name, str):
            raise ValueError("Last name is required")
        if len(last_name) > 50:
            raise ValueError("Character limit is 50")
        self.last_name = last_name
        
        #  Validate email
        if not isinstance(email, str):
            raise ValueError("Email is required")
        
        
        #  the code for standard email format
        email_regex = r"^[\w\.-]+@[\w\.-]+\.\w+$"
        if not re.match(email_regex, email):
            raise ValueError("Invalid email format")
        
        #  check for copies of email(s)
        if email in User.email:
            raise ValueError("Email already exist")

        #  assign email
        self.email = email
        
        self.role = role

    def is_admin(user):
        if user.role == "admin":
            print("Welcome admin")
        else:
            return "Access denied",
    def created_at():
        pass

    def updated_at():
        pass
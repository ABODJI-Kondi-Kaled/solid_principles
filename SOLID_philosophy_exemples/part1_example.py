# This script demonstrates the SOLID principles in Python with examples.
# Check the README.md file for more information.


# 1- Single Responsibility (SRP)

# ❌ Bad Practice: A class that violates SRP
class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email

    def get_user_info(self):
        return f"Name: {self.name}, Email: {self.email}"

    def send_email(self, message):
        # Simulate sending an email
        print(f"Sending email to {self.email}: {message}")

    def save_to_database(self):  
        print(f"Sauvegarde de {self.name} en DB...")

# ✅ Good Practice: Separate classes for different responsibilities
class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email

    def get_user_info(self):
        return f"Name: {self.name}, Email: {self.email}"
    
class EmailService:
    def send_email(self, email, message):
        # Simulate sending an email
        print(f"Sending email to {email}: {message}")

class DatabaseService:
    def save_user(self, user):
        print(f"Sauvegarde de {user.name} en DB...")

# 2- Open/Closed Principle (OCP)
# ❌ Bad Practice: A class that violates OCP
class Discount:  
    def apply(self, price, user_type):  
        if user_type == "premium":  
            return price * 0.8
        elif user_type == "regular":
            return price * 0.9
        elif user_type == "student":
            return price * 0.85
# ✅ Good Practice: Using polymorphism to extend functionality
class Discount:
    def apply(self, price):
        return price
class PremiumDiscount(Discount):
    def apply(self, price):
        return price * 0.8
class RegularDiscount(Discount):
    def apply(self, price):
        return price * 0.9
class StudentDiscount(Discount):
    def apply(self, price):
        return price * 0.85
# 3- Liskov Substitution Principle (LSP)
# ❌ Bad Practice: A class that violates LSP
class Bird:
    def fly(self):
        print("Flying")
class Ostrich(Bird): # Ostrich is a bird but cannot fly
    def fly(self):
        raise Exception("Ostriches can't fly, they run instead")
class Penguin(Bird): # Penguin is a bird but cannot fly
    def fly(self):
        raise Exception("Penguins can't fly, it swims instead")
    
# ✅ Good Practice: A class that adheres to LSP
class Bird:
    def move(self):
        print("Moving")
class Sparrow(Bird):
    def move(self):
        print("Flying")
class Ostrich(Bird):
    def move(self):
        print("Running")
class Penguin(Bird):
    def move(self):
        print("Swimming")
               
# 4- Interface Segregation Principle (ISP)
# ❌ Bad Practice: A class that violates ISP
class Printer:
    def print(self, document):
        print(f"Printing {document}")
    def scan(self, document):
        print(f"Scanning {document}")
    def fax(self, document):
        print(f"Faxing {document}")
# ✅ Good Practice: Separate interfaces for different functionalities
class Printer:
    def print(self, document):
        print(f"Printing {document}")


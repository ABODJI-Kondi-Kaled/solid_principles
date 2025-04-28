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



from userdb import User
from faker import Faker

faker=Faker()

def generate_random_users(num_users):
    for _ in range(num_users):
        username = faker.user_name()
        password = faker.password()
        email = faker.email()
        phone = faker.phone_number()
        is_admin = False 
        user = User(username, password, email, phone, is_admin)
        user.create_user()

# Generate 5 random users
generate_random_users(5)
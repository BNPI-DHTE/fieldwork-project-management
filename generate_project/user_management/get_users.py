import csv
import settings
from generate_project.user_management.User import User
from generate_project.user_management.validate_user_data import is_user_data_valid


def get_users_from_csv(users=settings.users_file):
    with open(users, 'r') as users_data:
        users_data = list(csv.DictReader(users_data))
        list_of_users = []
        for user_data in users_data:
            user = User(user_data)
            if is_user_data_valid(user_data):
                print(user)
                list_of_users.append(user)
        return users

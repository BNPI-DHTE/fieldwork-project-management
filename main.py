import logging
import settings
import generate_project.user_management.get_users as get_users


def create_projects():
    return None


def main():
    logging.basicConfig(format='%(asctime)s:(%(levelname)s) %(message)s',
                        filename='management.log',
                        encoding='utf-8',
                        level=logging.INFO)
    users = get_users.get_users_from_csv()


if __name__ == '__main__':
    main()

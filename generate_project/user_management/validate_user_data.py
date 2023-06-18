import logging


def is_user_data_valid(user_data):
    print(user_data)
    for key in user_data:
        if ((key != 'username') or (key != 'initial') or (key != 'device') or (key != 'variant'))\
                and (''.__eq__(user_data[key].strip())):
            logging.warning('User data %s is invalid at key %s', user_data, key)
            return False
    return True

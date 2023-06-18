from generate_project.user_management.validate_user_data import is_user_data_valid

valid_user_data = {'username': 'Bilbo Baggings', 'initial': 'BB', 'device': 'phone', 'variant': 'type02'}
invalid_user_data = {'username': 'Bilbo Baggings', 'initial': 'BB', 'device': '', 'variant': 'type02'}


def test_user_data_is_valid():
    assert is_user_data_valid(valid_user_data) is True


def test_user_data_is_invalid():
    assert is_user_data_valid(invalid_user_data) is False

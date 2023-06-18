from dataclasses import dataclass


@dataclass
class User:
    username: str
    initial: str
    device: str
    variant: str

    def __init__(self, user_data):
        for key in user_data:
            setattr(self, key, user_data[key])

import random
import string
from datetime import datetime, timedelta


class Helpers:

    @staticmethod
    def generate_random_string(length=10):
        
        return "".join(random.choice(string.ascii_lowercase) for i in range(length))

    @staticmethod
    def generate_tomorrow_date_Y_m_d():
        
        return (datetime.now() + timedelta(days=1)).strftime("%Y.%m.%d")

    @staticmethod
    def generate_payload_registration(length=10):
        
        return{
        "login": Helpers.generate_random_string(length),
        "password": Helpers.generate_random_string(length),
        "firstName": Helpers.generate_random_string(length)
        }
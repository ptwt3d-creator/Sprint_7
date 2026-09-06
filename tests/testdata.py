import requests
import random
import string
from url import Url
from datetime import datetime, timedelta


class TestData:

    tomorrow = (datetime.now() + timedelta(days=1)).strftime("%Y.%m.%d")

    # метод регистрации нового курьера возвращает список из логина и пароля
    # если регистрация не удалась, возвращает пустой список
    @staticmethod
    def generate_random_string(length):
        letters = string.ascii_lowercase
        random_string = "".join(random.choice(letters) for i in range(length))
        return random_string

    @staticmethod
    def register_new_courier_returns_dict_login_password_name(length):
        # создаём словарь, чтобы метод мог его вернуть
        reg_pass_data = {}
       
        # генерируем логин, пароль и имя курьера
        login = TestData.generate_random_string(length)
        password = TestData.generate_random_string(length)
        first_name = TestData.generate_random_string(length)

        # собираем тело запроса
        payload = {
            "login": login,
            "password": password,
            "firstName": first_name
        }
        # отправляем запрос на регистрацию курьера и сохраняем ответ в переменную response
        response = requests.post(Url.REGISTRATION_COURIER, data=payload)

        # если регистрация прошла успешно (код ответа 201), добавляем в словарь логин и пароль, имя курьера
        if response.status_code == 201:
            reg_pass_data = payload
        # возвращаем словарь
        return reg_pass_data 
    
    @staticmethod
    def register_new_courier_random_string_data(length):
        # генерируем логин, пароль и имя курьера
        login = TestData.generate_random_string(length)
        password = TestData.generate_random_string(length)
        first_name = TestData.generate_random_string(length)

        # собираем тело запроса
        payload = {
            "login": login,
            "password": password,
            "firstName": first_name
        }

        # отправляем запрос на регистрацию курьера и сохраняем ответ в переменную response
        requests.post(Url.REGISTRATION_COURIER, data=payload)

        return login, password

    @staticmethod
    def order_create(*, 
        firstName = "Вася",
        lastName = "Климкин",
        address = "Москва",
        metroStation = "Лубянка",
        phone = "88003553555",
        rentTime = 3,
        deliveryDate = None,
        comment = "бизнес",
        is_color_black = "False",
        is_color_gray = "False"):
        
        if deliveryDate is None:
            deliveryDate = TestData.tomorrow
        
        payload = {
            "firstName": firstName,
            "lastName": lastName,
            "address": address,
            "metroStation": metroStation,
            "phone": phone,
            "rentTime": rentTime,
            "deliveryDate": deliveryDate,
            "comment": comment,
            "color": [is_color_black, is_color_gray]
        }
        return payload
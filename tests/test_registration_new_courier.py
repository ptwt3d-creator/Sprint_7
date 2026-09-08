import requests
from data import TestData, TestUrl
import pytest
import allure
from helpers import Helpers
from api import ApiRequests


@allure.suite("Проверки регистрации курьера")
@allure.sub_suite("Регистрация курьера")
class TestRegistrationCourier:
    
    @allure.title("Успешная регистрация курьера со всеми обязательными полями")
    @allure.description("Проверяем, что передача валидных случайных строк в login, password и firstName возвращает код 201.")
    def test_register_new_courier_returns_201(self, cleanup_courier_and_check):

        payload = Helpers.generate_payload_registration()

        r = ApiRequests.register_courier(payload)

        cleanup_courier_and_check(payload)
        assert r.status_code == 201

    @allure.title("Успешная регистрация курьера со всеми обязательными полями")
    @allure.description("Проверяем, что передача валидных случайных строк в login, password и firstName возвращает тело успешного ответа {'ok': true}.")
    def test_register_new_courier_returns_successful_response_body(self, cleanup_courier_and_check):
        
        payload = Helpers.generate_payload_registration()

        r = ApiRequests.register_courier(payload)

        cleanup_courier_and_check(payload)
        assert r.json() == {"ok": True}

    @allure.title("Попытка регистрации дубликата курьера")
    @allure.description("Проверяем, что при попытке зарегистрировать пользователя с уже существующим в базе логином возвращается код 409.")
    def test_register_courier_with_taken_login_return_409(self, register_courier_returns_dict_login_password_firstName):
        
        reg_data = register_courier_returns_dict_login_password_firstName

        payload = {
            "login": reg_data["login"],
            "password": Helpers.generate_random_string(),
            "firstName": Helpers.generate_random_string()
        }

        # отправляем запрос на регистрацию курьера и сохраняем ответ в переменную r
        r = ApiRequests.register_courier(payload)

        assert r.status_code == 409
    
    @allure.title("Успешная регистрация курьера без указания имени")
    @allure.description("Проверяем граничное условие: поле firstName является необязательным, аккаунт должен успешно создаваться с пустой строкой.")
    def test_registration_without_firstName_returns_201(self, cleanup_courier_and_check):
        
        reg_data = Helpers.generate_payload_registration()

        payload = {
            "login": reg_data["login"],
            "password": reg_data["password"],
            "firstName": ""
        }

        r = ApiRequests.register_courier(payload)

        cleanup_courier_and_check(payload)
        assert r.status_code == 201

    @allure.title("Попытка регистрации без логина")
    @allure.description("Проверяем, что попытка регистрации курьера с пустым полем login возвращает код 400.")
    def test_registration_without_login_returns_400(self):
        
        reg_data = Helpers.generate_payload_registration()

        payload = {
            "login": "",
            "password": reg_data["password"],
            "firstName": reg_data["firstName"]
        }

        r = ApiRequests.register_courier(payload)

        assert r.status_code == 400

    @allure.title("Попытка регистрации без пароля")
    @allure.description("Проверяем, что попытка регистрации курьера с пустым полем password возвращает код 400.")
    def test_registration_without_password_returns_400(self):
        
        reg_data = Helpers.generate_payload_registration()

        payload = {
            "login": reg_data["login"],
            "password": "",
            "firstName": reg_data["firstName"]
        }

        r = ApiRequests.register_courier(payload)

        assert r.status_code == 400

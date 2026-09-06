import requests
from testdata import TestData
from url import Url
import pytest
import allure


@allure.suite("Проверки регистрации курьера")
@allure.sub_suite("Регистрация курьера")
class TestRegistrationCourier:
    
    @allure.title("Успешная регистрация курьера со всеми обязательными полями")
    @allure.description("Проверяем, что передача валидных случайных строк в login, password и firstName возвращает код 201 и ответ {'ok': true}.")
    def test_register_new_courier_returns_201(self):

        # генерируем логин, пароль и имя курьера
        login = TestData.generate_random_string(10)
        password = TestData.generate_random_string(10)
        first_name = TestData.generate_random_string(10)

        # собираем тело запроса
        payload = {
            "login": login,
            "password": password,
            "firstName": first_name
        }

        # отправляем запрос на регистрацию курьера и сохраняем ответ в переменную response
        response = requests.post(Url.REGISTRATION_COURIER, data=payload)

        # если регистрация прошла успешно - код ответа 201
        assert response.status_code == 201 and response.json() == {"ok": True}
    
    @allure.title("Успешная регистрация курьера без указания имени")
    @allure.description("Проверяем граничное условие: поле firstName является необязательным, аккаунт должен успешно создаваться с пустой строкой.")
    def test_registration_without_first_name_returns_201(self):
        
        login = TestData.generate_random_string(10)
        password = TestData.generate_random_string(10)
        first_name = ""

        payload = {
            "login": login,
            "password": password,
            "first_name": first_name
        }

        response = requests.post(Url.REGISTRATION_COURIER, data=payload)

        assert response.json() == {"ok": True}

    @allure.title("Попытка регистрации дубликата курьера")
    @allure.description("Проверяем, что при попытке зарегистрировать пользователя с уже существующим в базе логином возвращается код 409.")
    def test_register_two_courier_with_identical_random_login(self):

        # генерируем логин, пароль и имя курьера
        login = TestData.generate_random_string(10)
        password = TestData.generate_random_string(10)
        first_name = TestData.generate_random_string(10)

        # собираем тело запроса
        payload = {
            "login": login,
            "password": password,
            "firstName": first_name
        }

        # отправляем запрос на регистрацию курьера и сохраняем ответ в переменную response
        requests.post(Url.REGISTRATION_COURIER, data=payload, timeout=15)

        # Меняем имя и пароль оставляем логин
        payload["password"] = TestData.generate_random_string(10)
        payload["first_name"] = TestData.generate_random_string(10)  

        response = requests.post(Url.REGISTRATION_COURIER, data=payload)

        assert response.status_code == 409 and response.json().get("message") == "Этот логин уже используется. Попробуйте другой." # СООБЩЕНИЕ В ДОКУМЕНТАЦИИ ОТЛИЧАЕТСЯ.

    @allure.title("Попытка регистрации без логина")
    @allure.description("Проверяем, что попытка регистрации курьера с пустым полем login возвращает код 400 и валидный message.")
    def test_registration_without_login_returns_400(self):
        
        login = ""
        password = TestData.generate_random_string(10)
        first_name = TestData.generate_random_string(10)

        payload = {
            "login": login,
            "password": password,
            "first_name": first_name
        }

        response = requests.post(Url.REGISTRATION_COURIER, data=payload)

        assert response.status_code == 400 and response.json().get("message") == "Недостаточно данных для создания учетной записи"

    @allure.title("Попытка регистрации без пароля")
    @allure.description("Проверяем, что попытка регистрации курьера с пустым полем password возвращает код 400.")
    def test_registration_without_password_returns_400(self):
        
        login = TestData.generate_random_string(10)
        password = ""
        first_name = TestData.generate_random_string(10)

        payload = {
            "login": login,
            "password": password,
            "first_name": first_name
        }

        response = requests.post(Url.REGISTRATION_COURIER, data=payload)

        assert response.status_code == 400 and response.json().get("message") == "Недостаточно данных для создания учетной записи"

    

        
        

    
    
    
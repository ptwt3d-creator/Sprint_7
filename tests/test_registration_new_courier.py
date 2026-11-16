import requests
import pytest
import allure
from helpers import Helpers
from api import ApiRequests


@allure.suite("Проверки регистрации курьера")
@allure.sub_suite("Регистрация курьера")
class TestRegistrationCourier:
    
    @allure.title("Успешная регистрация курьера со всеми обязательными полями")
    @allure.description("Проверяем, что передача валидных случайных строк в login, password и firstName возвращает код 201.")
    def test_register_new_courier_returns_201_body(self, request, cleanup_courier):

        payload = Helpers.generate_payload_registration()
        request.node.courier_payload = payload

        r = ApiRequests.register_courier(payload)

        assert r.status_code == 201 and r.json() == {"ok": True}

    @allure.title("Попытка регистрации дубликата курьера")
    @allure.description("Проверяем, что при попытке зарегистрировать пользователя с уже существующим в базе логином возвращается код 409.")
    def test_register_courier_with_taken_login_return_409_body(self, request, cleanup_courier):
        request.node.courier_payload = []

        # регистрация курьера
        # нельзя использовать одно имя "payload" или прошлые словари будут перезаписаны в request.node(конкретно сейчас) тк они переданы ссылками
        payload_1 = Helpers.generate_payload_registration()
        request.node.courier_payload.append(payload_1)

        r = ApiRequests.register_courier(payload_1)

        # регистрация второго курьера с тем же логином
        payload_2 = {
            "login": payload_1["login"],
            "password": Helpers.generate_random_string(),
            "firstName": Helpers.generate_random_string()
        }
        request.node.courier_payload.append(payload_2)

        r = ApiRequests.register_courier(payload_2)

        assert r.status_code == 409 and r.json().get("message") == "Этот логин уже используется"
    
    @allure.title("Успешная регистрация курьера без указания имени")
    @allure.description("Проверяем граничное условие: поле firstName является необязательным, аккаунт должен успешно создаваться с пустой строкой.")
    def test_registration_without_firstName_returns_201_body(self, request, cleanup_courier):
        
        reg_data = Helpers.generate_payload_registration()

        payload = {
            "login": reg_data["login"],
            "password": reg_data["password"],
            "firstName": ""
        }
        request.node.courier_payload = payload

        r = ApiRequests.register_courier(payload)

        assert r.status_code == 201 and r.json() == {"ok": True}

    @allure.title("Попытка регистрации без логина")
    @allure.description("Проверяем, что попытка регистрации курьера с пустым полем login возвращает код 400.")
    def test_registration_without_login_returns_400_body(self, request, cleanup_courier):
        
        reg_data = Helpers.generate_payload_registration()

        payload = {
            "login": "",
            "password": reg_data["password"],
            "firstName": reg_data["firstName"]
        }
        request.node.courier_payload = payload

        r = ApiRequests.register_courier(payload)

        assert r.status_code == 400 and r.json().get("message") == "Недостаточно данных для создания учетной записи"

    @allure.title("Попытка регистрации без пароля")
    @allure.description("Проверяем, что попытка регистрации курьера с пустым полем password возвращает код 400.")
    def test_registration_without_password_returns_400_body(self, request, cleanup_courier):
        
        reg_data = Helpers.generate_payload_registration()

        payload = {
            "login": reg_data["login"],
            "password": "",
            "firstName": reg_data["firstName"]
        }
        request.node.courier_payload = payload

        r = ApiRequests.register_courier(payload)

        assert r.status_code == 400 and r.json().get("message") == "Недостаточно данных для создания учетной записи"

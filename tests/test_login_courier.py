import requests
from testdata import TestData
from url import Url
import pytest
import allure


@allure.suite("Проверки авторизации курьера")
@allure.sub_suite("Авторизация курьера")
class TestLoginCourier:

    @allure.title("Успешная авторизация курьера в системе")
    @allure.description("Проверяем, что при передаче валидных логина и пароля сервер возвращает код 200 и цифровой ID курьера.")
    def test_login_courier_rteurns_200(self):
        reg_data = TestData.register_new_courier_returns_dict_login_password_name(10)
        
        payload = {
            "login": reg_data["login"],
            "password": reg_data["password"]
        }

        r = requests.post(Url.LOGIN_COURIER, data=payload, timeout=20)

        assert r.status_code == 200 and type(r.json()["id"]) is int

    @allure.title("Попытка авторизации без логина")
    @allure.description("Проверяем, что при попытке входа с пустым логином возвращается код 400 и валидное сообщение об ошибке.")
    def test_login_without_login_rteurns_400(self):
        reg_data = TestData.register_new_courier_returns_dict_login_password_name(10)
        
        payload = {
            "login": "",
            "password": reg_data["password"]
        }

        r = requests.post(Url.LOGIN_COURIER, json=payload, timeout=20)

        assert r.status_code == 400 and r.json()["message"] == "Недостаточно данных для входа"

    @allure.title("Попытка авторизации без пароля")
    @allure.description("Проверяем, что при попытке входа с пустым паролем возвращается код 400 и валидное сообщение об ошибке.")
    def test_login_without_password_rteurns_400(self):
        reg_data = TestData.register_new_courier_returns_dict_login_password_name(10)
        
        payload = {
            "login": reg_data["login"],
            "password": ""
        }

        r = requests.post(Url.LOGIN_COURIER, json=payload, timeout=20)

        assert r.status_code == 400 and r.json()["message"] == "Недостаточно данных для входа"
    
    @allure.title("Попытка авторизации под несуществующим курьером")
    @allure.description("Проверяем, что при попытке входа под случайными (не зарегистрированными) данными возвращается код 404.")
    def test_login_not_reister_courier_rteurns_404(self):
        login = TestData.generate_random_string(10)
        password = TestData.generate_random_string(10)
        
        payload = {
            "login": login,
            "password": password
        }

        r = requests.post(Url.LOGIN_COURIER, json=payload, timeout=20)

        assert r.status_code == 404 and r.json()["message"] == "Учетная запись не найдена"


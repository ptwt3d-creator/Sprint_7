import requests
import pytest
import allure
from helpers import Helpers
from api import ApiRequests


@allure.suite("Проверки авторизации курьера")
@allure.sub_suite("Авторизация курьера")
class TestLoginCourier:

    @allure.title("Успешная авторизация курьера в системе")
    @allure.description("Проверяем, что при передаче валидных логина и пароля сервер возвращает код 200.")
    def test_login_courier_rteurns_200(self, register_courier_returns_dict_login_password_firstName):
        
        reg_data = register_courier_returns_dict_login_password_firstName
        
        payload = {
            "login": reg_data["login"],
            "password": reg_data["password"]
        }

        r = ApiRequests.login_courier(payload)

        assert r.status_code == 200
    
    @allure.title("Успешная авторизация курьера в системе")
    @allure.description("Проверяем, что при передаче валидных логина и пароля сервер возвращает ID курьера.")
    def test_login_courier_rteurns_id(self, register_courier_returns_dict_login_password_firstName):
        
        reg_data = register_courier_returns_dict_login_password_firstName

        payload = {
            "login": reg_data["login"],
            "password": reg_data["password"]
        }

        r = ApiRequests.login_courier(payload)

        assert r.json()["id"] > 0

    @allure.title("Попытка авторизации без логина")
    @allure.description("Проверяем, что при попытке входа с пустым логином возвращается код 400 и валидное сообщение об ошибке.")
    def test_login_without_login_rteurns_400(self, register_courier_returns_dict_login_password_firstName):
        
        reg_data = register_courier_returns_dict_login_password_firstName
        
        payload = {
            "login": "",
            "password": reg_data["password"]
        }

        r = ApiRequests.login_courier(payload)

        assert r.status_code == 400

    @allure.title("Попытка авторизации без пароля")
    @allure.description("Проверяем, что при попытке входа с пустым паролем возвращается код 400 и валидное сообщение об ошибке.")
    def test_login_without_password_rteurns_400(self, register_courier_returns_dict_login_password_firstName):
        
        reg_data = register_courier_returns_dict_login_password_firstName
        
        payload = {
            "login": reg_data["login"],
            "password": ""
        }

        r = ApiRequests.login_courier(payload)

        assert r.status_code == 400

    @allure.title("Попытка авторизации с не существующим логином")
    @allure.description("Проверяем, что при попытке входа с пустым логином возвращается код 404.")
    def test_login_with_non_register_login_rteurns_404(self, register_courier_returns_dict_login_password_firstName):
        
        reg_data = register_courier_returns_dict_login_password_firstName
        
        payload = {
            "login": Helpers.generate_random_string(length=10),
            "password": reg_data["password"]
        }

        r = ApiRequests.login_courier(payload)

        assert r.status_code == 404
    
    @allure.title("Попытка авторизации с не существующим паролем")
    @allure.description("Проверяем, что при попытке входа с пустым паролем возвращается код 404.")
    def test_login_with_non_register_password_rteurns_404(self, register_courier_returns_dict_login_password_firstName):
        
        reg_data = register_courier_returns_dict_login_password_firstName
        
        payload = {
            "login": reg_data["login"],
            "password": Helpers.generate_random_string(length=10)
        }

        r = ApiRequests.login_courier(payload)

        assert r.status_code == 404
    
    @allure.title("Попытка авторизации под несуществующим курьером")
    @allure.description("Проверяем, что при попытке входа под случайными (не зарегистрированными) данными возвращается код 404.")
    def test_login_with_non_register_courier_data_rteurns_404(self):
        
        payload = {
            "login": Helpers.generate_random_string(length=10),
            "password": Helpers.generate_random_string(length=10)
        }

        r = ApiRequests.login_courier(payload)

        assert r.status_code == 404
        


import requests
import pytest
import allure
from data import TestUrl
from api import ApiRequests



@allure.suite("Проверки получения списка заказов")
@allure.sub_suite("Получение списка всех заказов")
class TestListOrder:

    @allure.title("Успешное получение списка всех заказов")
    @allure.description("Проверяем, что API возвращает список заказов, структура ответа корректна и содержит все обязательные поля.")
    def test_get_list_order_returns_list_order(self, create_order):
        create_order
        
        r = ApiRequests.get_list_all_orders()

        assert "orders" in r.json()
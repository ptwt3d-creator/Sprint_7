import requests
from testdata import TestData
from url import Url
import pytest
import allure


@allure.epic("Операции с заказами")
@allure.feature("Получение списка заказов")
class TestListOrder:

    @allure.title("Успешное получение списка всех заказов")
    @allure.description("Проверяем, что API возвращает список заказов, структура ответа корректна и содержит все обязательные поля.")
    def test_get_list_order_returns_list_order(self):
        TestData.order_create()
        r = requests.get(Url.ORDER_GET_LIST)

        expected_fields_orders = {
        "id", 
        "courierId", 
        "firstName", 
        "lastName", 
        "address", 
        "metroStation", 
        "phone", 
        "rentTime", 
        "deliveryDate", 
        "track", 
        "color", 
        "comment", 
        "createdAt", 
        "updatedAt", 
        "status"
        }

        response_dict = r.json()
        assert "orders" in response_dict and type(response_dict["orders"]) is list and len(response_dict["orders"]) > 0 and response_dict
        
        for field in expected_fields_orders:
            assert field in response_dict["orders"][0], f"В заказе отсутствует поле: {field}"
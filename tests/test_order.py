import requests
from testdata import TestData
from url import Url
import pytest
import allure


@allure.suite("Проверки создания заказов")
@allure.sub_suite("Создание заказа")
class TestOrder:

    @allure.title("Создание заказа при"+" {test_name} "+"цвета.")
    @allure.description("Параметризованный тест: проверяем успешное создание заказа при"+" {test_name} "+"цвета.")
    @pytest.mark.parametrize(
        "test_name, is_color_black, is_color_gray",
        [
            ("выборе черного и белого", True, True),
            ("выборе белого", False, True),
            ("выборе черного", True, False),
            ("отсутствии выбора", False, False)
        ] 
    )
    def test_color_order(self, test_name, is_color_black, is_color_gray):
        payload = TestData.order_create(is_color_black = is_color_black, is_color_gray = is_color_gray)

        response = requests.post(Url.ORDER_CREATE, data=payload)

        assert response.status_code == 201 and type(response.json()["track"]) is int 


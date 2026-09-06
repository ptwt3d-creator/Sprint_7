import requests
from testdata import TestData
from url import Url
import pytest
import allure


@allure.epic("Операции с заказами")
@allure.feature("Создание заказа")
class TestOrder:

    @allure.title("Создание заказа с различными параметрами цвета самоката")
    @allure.description("Параметризованный тест: проверяем успешное создание заказа при выборе черного, серого, обоих цветов или без указания цвета.")
    @pytest.mark.parametrize(
        "name_test, is_color_black, is_color_gray",
        [
            ("1", True, True),
            ("1", False, True),
            ("1", True, False),
            ("1", False, False)
        ] 
    )
    def test_color_order(self, name_test, is_color_black, is_color_gray):
        payload = TestData.order_create(is_color_black = is_color_black, is_color_gray = is_color_gray)

        response = requests.post(Url.ORDER_CREATE, data=payload)

        assert response.status_code == 201 and type(response.json()["track"]) is int 


import requests
from data import TestUrl
import pytest
import allure
from api import ApiRequests


@allure.suite("Проверки создания заказов")
@allure.sub_suite("Создание заказа")
class TestOrder:

    @allure.title("Создание заказа при"+" {test_name} "+"цвета.")
    @allure.description("Параметризованный тест: проверяем успешное создание заказа при"+" {test_name} "+"цвета.")
    @pytest.mark.parametrize(
        "test_name, colors",
        [
            ("выборе черного и белого", [True, True]),
            ("выборе белого", [False, True]),
            ("выборе черного", [True, False]),
            ("явном отсутствии выбора", [False, False])
        ] 
    )
    def test_color_order(self, test_name, colors, make_order_data_payload):
        payload = make_order_data_payload({"colors": [colors]})

        r = ApiRequests.order_create(payload)

        assert "track" in r.json()


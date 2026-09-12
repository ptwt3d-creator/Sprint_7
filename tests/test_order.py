import requests
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
    def test_color_order_returns_201_body(self, test_name, colors, make_order_data_payload):
        payload = make_order_data_payload({"colors": [colors]})

        r = ApiRequests.order_create(payload)

        body = r.json()
        assert r.status_code == 201 and body.get("track") is not None and body.get("track") > 0


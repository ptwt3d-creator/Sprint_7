import requests
from data import TestData, TestUrl
from helpers import Helpers
import pytest
from api import ApiRequests
import logging

logger = logging.getLogger(__name__)


@pytest.fixture
def register_courier_returns_dict_login_password_firstName():

    payload = Helpers.generate_payload_registration()

    ApiRequests.register_courier(payload)

    # возвращаем словарь login password firstName
    return payload
    
@pytest.fixture
def make_order_data_payload():

    def _wrapper_order(custom_data=None):
        
        payload = TestData.get_defoult_order_data()

        if custom_data != None:
            payload.update(custom_data)

        if payload["deliveryDate"] is None:
            payload["deliveryDate"] = Helpers.generate_tomorrow_date_Y_m_d()
            
        return payload
    return _wrapper_order

@pytest.fixture
def create_order(make_order_data_payload):
    
    payload = make_order_data_payload()

    r_create = ApiRequests.order_create(payload)

    track_order = r_create.json()["track"]

    return track_order

@pytest.fixture
def cleanup_courier(request):
    yield

    data = getattr(request.node, "courier_payload", None)
    if not data:
        return
    
    if isinstance(data, list):
        payloads = data
    else:
        payloads = [data]

    for payload in payloads:
        if not payload or not payload.get("login") or not payload.get("password"):
            continue

        try:
            r = ApiRequests.login_courier(payload)
            courier_id = r.json().get("id")

            if courier_id:
                ApiRequests.delet_courier(courier_id)
        except Exception as e:
            # logger отображается в allure report, error - уровень важности
            logger.error(f"Ошибка во время очистки курьера {payload.get('login')}: {e}")

import requests
from data import TestData, TestUrl
from helpers import Helpers
import pytest
from api import ApiRequests
    

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

    r_get_order_by_track = ApiRequests.get_order_by_track(track_order)

    assert r_create.status_code == 201 and r_get_order_by_track.status_code == 200 and r_get_order_by_track.json()["order"]["track"] == track_order

@pytest.fixture
def cleanup_courier_and_check():
    reg_data = {}

    def _wrapper_cleanup_courier(received_courier):
        reg_data.update(received_courier)

    yield _wrapper_cleanup_courier
    payload = {
        "login": reg_data["login"],
        "password": reg_data["password"]
    }
    
    r = ApiRequests.login_courier(payload)

    courier_id = r.json()["id"]
    r_del = ApiRequests.delet_courier(courier_id)
    r_login_after_del = ApiRequests.login_courier(payload)

    assert r_del.status_code == 200 and r_login_after_del.status_code == 404 and r_login_after_del.json()["message"] == "Учетная запись не найдена"
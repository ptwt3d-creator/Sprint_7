import requests
from data import TestData, TestUrl
import allure

class ApiRequests:

    @allure.step("GET /api/v1/orders (Получение списка всех заказов)")
    def get_list_all_orders():
        return requests.get(TestUrl.ORDER_GET_LIST)
    
    @allure.step("POST /api/v1/courier/login (Авторизация курьера)")
    def login_courier(payload):
        return requests.post(TestUrl.LOGIN_COURIER, data=payload)

    @allure.step("POST /api/v1/courier (Регистрация нового курьера)")
    def register_courier(payload):
        return requests.post(TestUrl.REGISTRATION_COURIER, data=payload)

    @allure.step("POST /api/v1/orders (Создание нового заказа)")
    def order_create(payload):
        return requests.post(TestUrl.ORDER_CREATE, data=payload)

    @allure.step("DELETE /api/v1/courier/:id (Удаление курьера)")
    def delet_courier(courier_id):
        return requests.delete(f"{TestUrl.DELETE_COURIER}{courier_id}")

    @allure.step("GET /api/v1/orders/track (Получение заказа по его трек номеру)")
    def get_order_by_track(track_order):
        return requests.get(TestUrl.GET_ORDER_BY_TRACK, params={"t": track_order})
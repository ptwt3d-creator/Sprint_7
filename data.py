

class TestUrl:

    LOGIN_COURIER = "https://qa-scooter.praktikum-services.ru/api/v1/courier/login"
    REGISTRATION_COURIER = "https://qa-scooter.praktikum-services.ru/api/v1/courier"
    DELETE_COURIER = "https://qa-scooter.praktikum-services.ru/api/v1/courier/" 
    ORDER_CREATE = "https://qa-scooter.praktikum-services.ru/api/v1/orders"
    ORDER_GET_LIST = "https://qa-scooter.praktikum-services.ru/api/v1/orders"
    GET_ORDER_BY_TRACK = "https://qa-scooter.praktikum-services.ru/api/v1/orders/track"


class TestData:

    @staticmethod
    def get_defoult_order_data():

        DEFAULT_ORDER_DATA = {
        "firstName": "Вася",
        "lastName": "Климкин",
        "address":  "Москва",
        "metroStation": "Лубянка",
        "phone": "88003553555",
        "rentTime": 3,
        "deliveryDate": None,
        "comment": "бизнес",
        "colors": [False, False]
        }

        return DEFAULT_ORDER_DATA.copy()
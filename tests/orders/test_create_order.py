import allure
import pytest
import data
from methods.order_methods import OrderMethods


class TestCreateOrder:
    @allure.title('Проверка создания заказа')
    @allure.description('Проверяем, что при заполнении всех обязательных полей и с разными вариантами цветов '
                        'происходит успешное создание заказа: статус 201 и тело ответа содержит "track"')
    @pytest.mark.parametrize('color', data.COLOR_COMBINATIONS)
    def test_post_create_order(self, color):
        payload = {
            "firstName": "Naruto",
            "lastName": "Uchiha",
            "address": "Konoha, 142 apt.",
            "metroStation": 4,
            "phone": "+7 800 355 35 35",
            "rentTime": 5,
            "deliveryDate": "2020-06-06",
            "comment": "Saske, come back to Konoha",
            "color": color
        }
        order_methods = OrderMethods()
        status_code, response_context = order_methods.post_create_order(payload)
        assert status_code == 201 and 'track' in response_context

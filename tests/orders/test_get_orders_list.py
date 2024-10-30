import allure
from methods.order_methods import OrderMethods


class TestGetOrdersList:
    @allure.title('Проверка получения списка заказов')
    @allure.description('Проверяем, что в тело ответа возвращается список заказов')
    def test_get_orders_list_response_contains_list_orders(self):
        order_methods = OrderMethods()
        assert type(order_methods.get_orders_list()["orders"]) == list

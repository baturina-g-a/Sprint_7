import allure
import requests
from data import BASE_URL, ORDERS_URL


class OrderMethods:

    @allure.step('Метод создания заказа - POST-запрос')
    def post_create_order(self, payload):
        response = requests.post(f'{BASE_URL}{ORDERS_URL}', json=payload)
        return response.status_code, response.json()

    @allure.step('Метод получения списка заказов - GET-запрос')
    def get_orders_list(self):
        response = requests.get(f'{BASE_URL}{ORDERS_URL}')
        return response.json()

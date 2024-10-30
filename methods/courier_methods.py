import allure
import requests
from data import BASE_URL, COURIER_URL


class CourierMethods:

    @allure.step('Метод создания курьера - POST-запрос')
    def post_create_courier(self, payload):
        response = requests.post(f'{BASE_URL}{COURIER_URL}', json=payload)
        return response.status_code, response.json()

    @allure.step('Метод логина курьера в системе - POST-запрос')
    def post_login_courier(self, payload):
        response = requests.post(f'{BASE_URL}{COURIER_URL}login', json=payload)
        return response.status_code, response.json()

    @allure.step('Метод удаления курьера - DELETE-запрос')
    def delete_courier(self, payload):
        login_payload = {"login": payload["login"], "password": payload["password"]}
        response_login = requests.post(f'{BASE_URL}{COURIER_URL}login', json=login_payload)
        courier_id = response_login.json()['id']
        delete_payload = {"id": courier_id}
        response = requests.delete(f'{BASE_URL}{COURIER_URL}:{courier_id}', json=delete_payload)
        return response.status_code

import allure
import data
import helpers
from methods.courier_methods import CourierMethods


class TestLoginCourier:

    @allure.title('Проверка логина курьера')
    @allure.description('Проверяем, что при заполнении всех обязательных полей происходит успешный логин курьера:'
                        'получаем правильный код ответа 200 и получаем "id" в теле ответа')
    def test_post_login_courier_success_with_all_required_fields_return_id(self):
        payload = data.EXISTING_USER
        courier_methods = CourierMethods()
        status_code, response_context = courier_methods.post_login_courier(payload)
        assert status_code == 200 and 'id' in response_context

    @allure.title('Проверка, что невозможен логин курьера с некорректным логином')
    @allure.description('Проверяем, что если в поле логина ввести несоответствующее значение, то логин курьера не '
                        'происходит, получаем: код ответа 404 и соответсвующее сообщение')
    def test_post_login_courier_with_invalid_login_returns_error(self):
        payload = {
            "login": helpers.register_new_courier_and_return_login_password()[0],
            "password": data.EXISTING_USER["password"]
        }
        courier_methods = CourierMethods()
        status_code, response_context = courier_methods.post_login_courier(payload)
        assert status_code == 404 and response_context["message"] == "Учетная запись не найдена"

    @allure.title('Проверка, что невозможен логин курьера с некорректным паролем')
    @allure.description('Проверяем, что если в поле пароля ввести несоответствующее значение, то логин курьера не '
                        'происходит, получаем: код ответа 404 и соответсвующее сообщение')
    def test_post_login_courier_with_invalid_password_returns_error(self):
        payload = {
            "login": data.EXISTING_USER["login"],
            "password": helpers.register_new_courier_and_return_login_password()[1]
        }
        courier_methods = CourierMethods()
        status_code, response_context = courier_methods.post_login_courier(payload)
        assert status_code == 404 and response_context["message"] == "Учетная запись не найдена"

    @allure.title('Проверка, что невозможен логин курьера без логина')
    @allure.description('Проверяем, что если не заполнить обязательное поле логина, то логин курьера не '
                        'происходит, получаем: код ответа 400 и соответсвующее сообщение')
    def test_post_login_courier_without_login_field_returns_error(self):
        payload = {
            "login": "",
            "password": data.EXISTING_USER["password"]
        }
        courier_methods = CourierMethods()
        status_code, response_context = courier_methods.post_login_courier(payload)
        assert status_code == 400 and response_context["message"] == "Недостаточно данных для входа"

    @allure.title('Проверка, что невозможен логин курьера без пароля')
    @allure.description('Проверяем, что если не заполнить обязательное поле пароля, то логин курьера не '
                        'происходит, получаем: код ответа 400 и соответсвующее сообщение')
    def test_post_login_courier_without_password_field_returns_error(self):
        payload = {
            "login": data.EXISTING_USER["login"],
            "password": ""
        }
        courier_methods = CourierMethods()
        status_code, response_context = courier_methods.post_login_courier(payload)
        assert status_code == 400 and response_context["message"] == "Недостаточно данных для входа"

    @allure.title('Проверка, что невозможен логин несуществующего курьера')
    @allure.description('Проверяем, что если заполнить обязательное поля логина и пароля несуществующими данными, '
                        'то логин курьера не происходит, получаем: код ответа 404 и соответсвующее сообщение')
    def test_post_login_courier_with_nonexistent_user_returns_error(self):
        payload = {
            "login": helpers.register_new_courier_and_return_login_password()[0],
            "password": helpers.register_new_courier_and_return_login_password()[1]
        }
        courier_methods = CourierMethods()
        status_code, response_context = courier_methods.post_login_courier(payload)
        assert status_code == 404 and response_context["message"] == "Учетная запись не найдена"

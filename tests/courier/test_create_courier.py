import allure
import data
import helpers
from methods.courier_methods import CourierMethods


class TestCreateCourier:

    @allure.title('Проверка регистрации курьера')
    @allure.description('Проверяем, что при заполнении всех обязательных полей происходит успешная регистрация курьера:'
                        'получаем правильный код ответа 201 и {"ok":true}')
    def test_post_create_courier_with_all_required_data_return_correct_code_and_text(self):
        payload = {
            "login": helpers.generate_random_string(10),
            "password": helpers.generate_random_string(10),
            "firstName": helpers.generate_random_string(10),
        }
        courier_methods = CourierMethods()
        status_code, response_context = courier_methods.post_create_courier(payload)
        courier_methods.delete_courier(payload)
        assert status_code == 201 and response_context == {'ok': True}

    @allure.title('Проверка, что нельзя создать двух одинаковых курьеров')
    @allure.description('Проверяем, что если создать пользователя с логином, который уже есть, возвращается ошибка: '
                        'получаем код ответа 409 и соответсвующее сообщение')
    def test_post_create_courier_cant_create_two_courier_with_same_login_returns_error(self):
        payload = {
            "login": data.EXISTING_USER["login"],
            "password": data.EXISTING_USER["password"]
        }
        courier_methods = CourierMethods()
        status_code, response_context = courier_methods.post_create_courier(payload)
        assert status_code == 409 and response_context["message"] == "Этот логин уже используется. Попробуйте другой."

    @allure.title('Проверка, что нельзя создать курьера без логина')
    @allure.description('Проверяем, что если не заполнить обязательное поле логина, то курьер не создается, получаем '
                        'код ответа 400 и соответсвующее сообщение')
    def test_post_create_courier_without_login_field_returns_error(self):
        payload = {
            "login": "",
            "password": helpers.generate_random_string(10),
            "firstName": helpers.generate_random_string(10),
        }
        courier_methods = CourierMethods()
        status_code, response_context = courier_methods.post_create_courier(payload)
        assert status_code == 400 and response_context["message"] == "Недостаточно данных для создания учетной записи"

    @allure.title('Проверка, что нельзя создать курьера без пароля')
    @allure.description('Проверяем, что если не заполнить обязательное поле пароля, то курьер не создается, получаем '
                        'код ответа 400 и соответсвующее сообщение')
    def test_post_create_courier_without_password_field_returns_error(self):
        payload = {
            "login": helpers.generate_random_string(10),
            "password": "",
            "firstName": helpers.generate_random_string(10),
        }
        courier_methods = CourierMethods()
        status_code, response_context = courier_methods.post_create_courier(payload)
        assert status_code == 400 and response_context["message"] == "Недостаточно данных для создания учетной записи"

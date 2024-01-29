import time

from pages.base_page import BasePage
from pages.locators import RegistrationFormPageLocators
from selenium.webdriver.support.ui import Select


class StudentRegistrationFormPage(BasePage):
    """Методы для взаимодействия со страницей регистрации"""

    def fill_firstname_field(self, data: str):
        """Действие: Заполнить поле Firstname"""
        self.send_data(RegistrationFormPageLocators.FIRSTNAME_FIELD, data)

    def fill_lastname_field(self, data: str):
        """Действие: Заполнить поле Lastname"""
        self.send_data(RegistrationFormPageLocators.LASTNAME_FIELD, data)

    def fill_user_email_field(self, data: str):
        """Действие: Заполнить поле UserEmail"""
        self.send_data(RegistrationFormPageLocators.MAIL_FIELD, data)

    def choice_gender(self, gender):
        """Действие: Выбрать радио-баттон Gender"""
        if gender == "Male":
            self.click_element(RegistrationFormPageLocators.RADIO_BUTTON_GENDER_MALE)
        elif gender == "Female":
            self.click_element(RegistrationFormPageLocators.RADIO_BUTTON_GENDER_FEMALE)
        elif gender == "Other":
            self.click_element(RegistrationFormPageLocators.RADIO_BUTTON_GENDER_OTHER)

    def fill_user_number_field(self, data: str):
        """Действие: Заполнить поле UserNumber"""
        self.send_data(RegistrationFormPageLocators.USER_NUMBER_FIELD, data)

    def choice_date_birthday(self, year, month):
        """
        Действие: Выбрать дату рождения в календаре
        Выбор года и месяца - через выпадающие списки
        """
        self.click_element(RegistrationFormPageLocators.DATE_OF_BIRTHDAY_CALENDAR)

        select_year = Select(self.wait_until_clickable(RegistrationFormPageLocators.YEAR_DROPDOWN_IN_CALENDAR))
        select_year.select_by_value(year)

        select_month = Select(self.wait_until_clickable(RegistrationFormPageLocators.MONTH_DROPDOWN_IN_CALENDAR))
        select_month.select_by_visible_text(month)

        self.click_element(RegistrationFormPageLocators.DAY_IN_CALENDAR)

    def fill_subjects_field(self, data: str):
        """Действие: Заполнить поле Subjects"""
        self.send_data(RegistrationFormPageLocators.SUBJECTS_FIELD, data)

    def fill_current_address_field(self, data: str):
        """Действие: Заполнить поле CurrentAddress"""
        self.send_data(RegistrationFormPageLocators.CURRENT_ADDRESS_FIELD, data)

    def choice_state(self, state: str):
        """Действие: Выбрать State"""
        self.click_element(RegistrationFormPageLocators.STATE_DROPDOWN)

        if state == "NCR":
            self.click_element(RegistrationFormPageLocators.STATE_NCR)
        elif state == "Uttar Pradesh":
            self.click_element(RegistrationFormPageLocators.STATE_UTTAR_PRADESH)
        elif state == "Haryana":
            self.click_element(RegistrationFormPageLocators.STATE_HARYANA)
        else:
            raise ValueError("Bad State")

    def choice_city(self):
        """Действие: Выбрать City"""
        self.click_element(RegistrationFormPageLocators.CITY_DROPDOWN)
        time.sleep(180)
        self.click_element(RegistrationFormPageLocators.CITY_0)

    def click_submit(self):
        """Действие: Клик по кнопке Submit"""
        self.click_element(RegistrationFormPageLocators.SUBMIT_BUTTON)

    def assert_modal_window_title(self):
        """Проверка того, что во всплывающем окне корректный заголовок"""
        modal_window_title = self.wait_until_visible(RegistrationFormPageLocators.MODAL_WINDOW_TITLE)
        assert modal_window_title.text == "Thanks for submitting the form", \
            f"Во всплывающем окне другой title: {modal_window_title.text}"

    def prepare_list_with_text_of_webelements(self, list_webelements: list):
        """
        Подготовка списка состоящего из webelement.text
        На вход получает список веб-элементов
        :param list_webelements:
        :return: список с текстовыми значениями, поданных на вход вэб-элементов
        """
        list_with_text_of_webelements = []
        for element in list_webelements:
            list_with_text_of_webelements.append(element.text)

        return list_with_text_of_webelements

    def prepare_user_parameter_from_modal_window(self):
        """
        Подготовка словаря с регистрационными данными, полученными из модального окна
        :return: dict, где: key - label из модального окна, value - values из модального окна
        """
        user_parameters_keys_webelements = self.browser.find_elements(
            *RegistrationFormPageLocators.MODAL_WINDOW_BODY_KEYS)
        user_parameters_keys = self.prepare_list_with_text_of_webelements(user_parameters_keys_webelements)

        user_parameters_values_webelements = self.browser.find_elements(
            *RegistrationFormPageLocators.MODAL_WINDOW_BODY_VALUES)
        user_parameters_values = self.prepare_list_with_text_of_webelements(user_parameters_values_webelements)

        return dict(zip(user_parameters_keys, user_parameters_values))

    def assert_modal_window_body(self, registration_data: dict):
        """Проверка того, что во всплывающем окне указаны данные которые вводили при регистрации"""
        # словарь с данными которые вводили при регистрации
        expected_reg_data = registration_data

        # словарь с регистрационными данными из модального окна
        actual_reg_data = self.prepare_user_parameter_from_modal_window()

        assert f"{expected_reg_data['firstname']} {expected_reg_data['lastname']}" == actual_reg_data["Student Name"], \
            f"Student Name '{actual_reg_data['Student Name']}' не соответствует значениям указанным при регистрации " \
            f"{expected_reg_data['firstname']} {expected_reg_data['lastname']}"

        assert expected_reg_data["user_email"] == actual_reg_data["Student Email"], \
            f"Student Email {actual_reg_data['Student Email']} не соответствует значению указанному при регистрации " \
            f"{expected_reg_data['user_email']}"

        assert expected_reg_data["gender"] == actual_reg_data["Gender"], \
            f"Gender {actual_reg_data['Gender']} не соответствует значению указанному при регистрации " \
            f"{expected_reg_data['gender']}"

        assert expected_reg_data["user_number"] == actual_reg_data["Mobile"], \
            f"Mobile {actual_reg_data['Mobile']} не соответствует значению указанному при регистрации " \
            f"{expected_reg_data['user_number']}"

        assert f"{expected_reg_data['date_birthday_day']} {expected_reg_data['date_birthday_month']}," \
               f"{expected_reg_data['date_birthday_year']}" == actual_reg_data['Date of Birth'], \
            f"Date of Birth {actual_reg_data['Date of Birth']} не соответствует значению указанному при регистрации " \
            f"{expected_reg_data['date_birthday_day']} {expected_reg_data['date_birthday_month']}," \
            f"{expected_reg_data['date_birthday_year']}"

        # assert expected_reg_data["current_address"] == actual_reg_data["Subjects"]

        # assert expected_reg_data["current_address"] == actual_reg_data["Hobbies"],

        # assert expected_reg_data["current_address"] == actual_reg_data["Picture"],

        assert expected_reg_data["current_address"] == actual_reg_data["Address"], \
            f"Address {actual_reg_data['Address']} не соответствует значению указанному при регистрации " \
            f"{expected_reg_data['current_address']}"

        # assert f"{expected_reg_data['state']} {expected_reg_data['city']}" == actual_reg_data["State and City"], f" {} не соответствует значению указанному при регистрации {}"

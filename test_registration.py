import time

from pages.locators import RegistrationFormPageLocators
from pages.student_registration_form_page import StudentRegistrationFormPage
from data import registration_user_link, registration_user_data

import os


def test_registration_form(browser):
    student_registration_page = StudentRegistrationFormPage(browser, registration_user_link)

    student_registration_page.fill_firstname_field(registration_user_data["firstname"])
    student_registration_page.fill_lastname_field(registration_user_data["lastname"])
    student_registration_page.fill_user_email_field(registration_user_data["user_email"])
    student_registration_page.choice_gender(registration_user_data["gender"])
    student_registration_page.fill_user_number_field(registration_user_data["user_number"])
    student_registration_page.choice_date_birthday(registration_user_data["date_birthday_year"],
                                                   registration_user_data["date_birthday_month"])
    student_registration_page.fill_subjects_field(registration_user_data["subjects"])

    current_dir = os.path.abspath(os.path.dirname(__file__))
    file_name = "picture.png"
    file_path = os.path.join(current_dir, file_name)
    student_registration_page.send_data(RegistrationFormPageLocators.SELECT_PICTURE, file_path)

    student_registration_page.fill_current_address_field(registration_user_data["current_address"])
    student_registration_page.choice_state(registration_user_data["state"])


    student_registration_page.choice_city()

    student_registration_page.click_submit()

    student_registration_page.assert_modal_window_title()
    student_registration_page.assert_modal_window_body(registration_user_data)

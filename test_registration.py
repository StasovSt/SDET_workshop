import pytest

from pages.student_registration_form_page import StudentRegistrationFormPage
from data_for_test import registration_user_link, registration_user_data


@pytest.mark.xfail(reason="Значение указываемое в поле 'subjects' не сохраняется")
def test_registration_form(browser):
    student_registration_page = StudentRegistrationFormPage(browser, registration_user_link)
    # step1
    student_registration_page.fill_firstname_field(registration_user_data["firstname"])
    # step2
    student_registration_page.fill_lastname_field(registration_user_data["lastname"])
    # step3
    student_registration_page.fill_user_email_field(registration_user_data["user_email"])
    # step4
    student_registration_page.choice_gender(registration_user_data["gender"])
    # step5
    student_registration_page.fill_user_number_field(registration_user_data["user_number"])
    # step6
    student_registration_page.choice_date_birthday(registration_user_data["date_birthday_year"],
                                                   registration_user_data["date_birthday_month"])
    # step7
    student_registration_page.fill_subjects_field(registration_user_data["subjects"])
    # step8
    student_registration_page.upload_file(registration_user_data["picture"])
    # step9
    student_registration_page.fill_current_address_field(registration_user_data["current_address"])
    # step10
    student_registration_page.choice_state(registration_user_data["state"])
    # step11
    student_registration_page.choice_city(registration_user_data["city"])
    # step12
    student_registration_page.click_submit()
    # asserts
    student_registration_page.assert_modal_window_title()
    student_registration_page.assert_modal_window_body(registration_user_data)

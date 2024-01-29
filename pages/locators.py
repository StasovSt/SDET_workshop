from selenium.webdriver.common.by import By
from data import registration_user_data


class RegistrationFormPageLocators:
    """Локаторы Student Registration Form"""

    # Поле для ввода firstName
    FIRSTNAME_FIELD = (By.ID, "firstName")

    # Поле для ввода lastName
    LASTNAME_FIELD = (By.ID, "lastName")

    # Поле для ввода userEmail
    MAIL_FIELD = (By.ID, "userEmail")

    # Радио-баттон gender - Male
    RADIO_BUTTON_GENDER_MALE = (By.XPATH, "//input[@value='Male']/..")

    # Радио-баттон gender - Female
    RADIO_BUTTON_GENDER_FEMALE = (By.XPATH, "//input[@value='Female']/..")

    # Радио-баттон gender - Other
    RADIO_BUTTON_GENDER_OTHER = (By.XPATH, "//input[@value='Other']/..")

    # Поле для ввода userNumber
    USER_NUMBER_FIELD = (By.ID, "userNumber")

    # Локатор календаря
    DATE_OF_BIRTHDAY_CALENDAR = (By.ID, "dateOfBirthInput")

    # Выпадающий список Года
    YEAR_DROPDOWN_IN_CALENDAR = (By.CSS_SELECTOR, ".react-datepicker__year-select")

    # Выпадающий список Месяца
    MONTH_DROPDOWN_IN_CALENDAR = (By.CSS_SELECTOR, ".react-datepicker__month-select")

    # Составной локатор дня в месяце. Окончание локатора берется из рег. данных (registration_user_data)
    DAY_IN_CALENDAR = (By.CSS_SELECTOR, f".react-datepicker__day--0{registration_user_data['date_birthday_day']}")

    # Поле для ввода subjectsInput
    SUBJECTS_FIELD = (By.ID, "subjectsInput")

    # Поле для загрузки картинки
    SELECT_PICTURE = (By.ID, "uploadPicture")

    # Поле для ввода currentAddress
    CURRENT_ADDRESS_FIELD = (By.ID, "currentAddress")

    # Выпадающий список State
    STATE_DROPDOWN = (By.ID, "state")

    # State - NSR
    STATE_NCR = (By.ID, "react-select-3-option-0")

    # State - Uttar Pradesh
    STATE_UTTAR_PRADESH = (By.ID, "react-select-3-option-1")

    # State - Haryana
    STATE_HARYANA = (By.ID, "react-select-3-option-2")

    # Выпадающий список City
    CITY_DROPDOWN = (By.ID, "city")

    # City -
    CITY_0 = (By.ID, "react-select-4-option-0")

    # Кнопка Submit
    SUBMIT_BUTTON = (By.ID, "submit")

    # Title модального окна
    MODAL_WINDOW_TITLE = (By.ID, "example-modal-sizes-title-lg")

    # Ключи модального окна (значения указанные при регистрации)
    MODAL_WINDOW_BODY_KEYS = (By.XPATH, "//div[@class='modal-body']//tr/td[1]")

    # Значения модального окна (значения указанные при регистрации)
    MODAL_WINDOW_BODY_VALUES = (By.XPATH, "//div[@class='modal-body']//tr/td[2]")

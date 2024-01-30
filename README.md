# autotests project for SDET-workshop from SimbirSoft 

## Описание проекта

- Автотест реализован в файле test_registration.py и помечен маркой XFAIL, так как при заполнении поля "Subjects" значение не сохраняется (bug is detected) и при последующем ассерте тест падает;
- Методы для взаимодействия с браузером реализованы в файлах _page.py (каталог pages);
- Локаторы веб-элементов реализованы в файле locators.py (каталог pages);
- Фикстура получения объекта webdriver реализована в файле conftest.py; Размер окна браузера задан кастомным для обхода перекрытия кнопки "Submit" футером (по сути это бага);
- В корне директории лежит картинка для использования теста (picture.png);
- Тестовые данные указаны в файле data_for_test.py

### Запуск автотестов
```sh
pip install requirements.txt
pytest -rx -v --alluredir=allure_results
```

### Открытие allure-отчета о результах теста
```sh
allure serve allure_results
```

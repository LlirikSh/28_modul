# 28_modul

Финальный тестовый проект SkillFactory курса QAP

Автоматизированное тестирование UI сайта: https://b2c.passport.rt.ru с использованием PyTest и Selenium.

С тест-кейсами можно ознакомиться по ссылке: https://docs.google.com/spreadsheets/d/1wVzwQnzjAwg10ZJz2vKkN35Pb3ZtTGXVlasppaHA4s8/edit?usp=sharing

Проект выполнен с использованием шаблона PageObject, Selenium и PyTest (Python)

В корне проекта в файле "config" прописаны:

-Путь к вебдрайверу. Чтобы запустить проект на другом компьютере, необходимо данный параметр изменить и прописать актуальный путь к драйверу для конкретного компьбтера.
-URL страниц сайта.
-Параметры размера экрана.


В папке pages в файле base_page.py находится конструктор webdriver и общие для всех тестируемых страниц методы.

В папке pages в файлах cart_page.py, main_page.py, search_page.py находятся методы для соответствующих тестируемых страниц.

В папке pages в файле "locators.py находятся все локаторы.

В корне проекта в файле conftest.py содержит фикстуру для настройки брайзера.

В корне проекта в файле pytest.ini зарегистрированны метки маркеровок тестов.

В корне проекта в файле requirements.py описаны используемые библиотеки.

В корне проекта в файлах test_cart_page.py, test_main_page.py, test_search_page.py находятся тесты. Все тесты помечены номером который совпадает с номером тест-кейса в файле: https://docs.google.com/spreadsheets/d/1ivsgIKMrdE2ECkFyFxpjPVEXgecPAIRF6Vv8-AXlkj4/edit?usp=sharing Во всех файлах с тестами находятся закомментированные команды для запуска тестов из командной строки (# pytest -v --tb=line test_main_page.py)

class TestData:
    # АДРЕС ДРАЙВЕРА
    CHROME_DRIVER_PATH = 'C:\\WebDriver\\bin\\chromedriver.exe'
    # URL личный кабинет "Ростелеком"
    START_URL = 'https://b2c.passport.rt.ru'

    # URL страниц кнопок/иконок в шапке сайта
    PUTORDER_URL = START_URL + 'cabinet/putorder/'
    CART_URL = START_URL + 'cart/'
    CALL_URL = START_URL + 'contact/'

    # URL страниц ссылок в шапке сайта
    BEST_URL = START_URL + 'best/'
    SCHOOL_URL = START_URL + 'school/'
    GAMES_URL = START_URL + 'games/'
    OFFICE_URL = START_URL + 'office/'
    CLUB_URL = START_URL + 'club/'

    # URL страниц разделов в поле под шапкой сайта
    DELIVERY_URL = START_URL + 'help/'
    SERTIFICATES_URL = START_URL + 'top/certificates/'
    RATING_URL = START_URL + 'rating/?id_genre=-1&nrd=1'
    NOVELTY_URL = START_URL + 'novelty/'
    DISCOUNT_URL = START_URL + 'search/?discount=1&available=1&order=actd&way=back&paperbooks=1&ebooks=1&otherbooks=1'
    CONTACT_URL = START_URL + 'contact/'
    SUPPORT_URL = START_URL + 'support/'
    MAPS_URL = START_URL + 'maps/'
    MOSCOW_DELIVERY_URL = MAPS_URL

    # URL страниц ссылок на главной странице сайта
    TOP_TOREAD_URL = START_URL + 'top/toread/'

    TEXT_BASE_PAGE = 'u"Лучшая покупка дня"'

    # атрибуты карточки товара
    TEXT_BTN_CART = 'В КОРЗИНУ'
    TEXT_BTN_CART_1 = 'ПРЕДЗАКАЗ'
    IMG_attribute = 'src'

    # Параметры размера открываемой страницы на экране
    WIDTH_WINDOW_1 = 1020
    LENGTH_WINDOW_1 = 900
    WIDTH_WINDOW = 1900
    LENGTH_WINDOW = 1000

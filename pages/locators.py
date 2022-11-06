class AuthLocators:
    # локатор логотипа "Лабиринт"
    AUTH_LOGO = (By.CLASS_NAME, "rt-logo main-header__logo")

    # Локатор кнопки "Телефон" на стартовой на странице
    AUTH_START_PHONE = (By.XPATH, '//span[text()="Телефон"]')
    # Локатор кнопки "Почта" на стартовой на странице
    AUTH_START_MAIL = (By.XPATH, '//span[text()="Почта"]')
    # Локатор кнопки "Логин" на стартовой на странице
    AUTH_START_LOGIN = (By.XPATH, '//span[text()="Логин"]')
    # Локатор кнопки "Лицевой счет" на стартовой на странице
    AUTH_START_PERSONAL_ACCOUNT = (By.XPATH, '//span[text()="Лицевой счёт"]')
    # Локатор кнопки социальных сетей "ВК" на стартовой на странице
    AUTH_START_VK = (By.XPATH, '//div[@class="social-providers"]/a[@alt="ВКонтакте"]')
    # Локатор кнопки социальных сетей "Однокласники" на стартовой на странице
    AUTH_START_OK = (By.XPATH, '//div[@class="social-providers"]/a[@alt="Одноклассники.ru"]')
    # Локатор кнопки социальных сетей "Мой мир" на стартовой на странице
    AUTH_START_MY_WORLD = (By.XPATH, '//div[@class="social-providers"]/a[@alt="Mail.ru"]')
    # Локатор кнопки социальных сетей "Google" на стартовой на странице
    AUTH_START_GOOGLE = (By.XPATH, '//div[@class="social-providers"]/a[@alt="Google+"]')
    # Локатор кнопки социальных сетей "Яндекс" на стартовой на странице
    AUTH_START_YANDEX = (By.XPATH, '//div[@class="social-providers"]/a[@alt="Yandex.ru"]')
    # Локатор кнопки "Регистрация" на стартовой на странице
    AUTH_START_REGISTER = (By.XPATH, '//div[@class="login-form__register-con"]/a[text()=" Зарегистрироваться "]')
    # Локатор кнопки "Чат" на стартовой на странице
    AUTH_START_CHAT = (By.CLASS_NAME, "omnichat-bar-root svelte-16eyo30")
    # Локатор кнопки "Забыл пароль" на стартовой на странице
    AUTH_START_FORGOT_PASSWORD =  (By.CLASS_NAME, "b-header-b-personal-e-list-item")
    # Локатор кнопки "Войти" на стартовой на странице
    AUTH_START_LOGIN = (By.CLASS_NAME, "rt-link rt-link--orange rt-link--muted login-form__forgot-pwd login-form__forgot-pwd--muted")
    # Локатор кнопки "Пользовательское соглашение" на стартовой на странице
    AUTH_START_USER_AGREEMENT = (By.XPATH, '//div[@class="auth-policy"]/a[text()="пользовательского соглашения"]')  

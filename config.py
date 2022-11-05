class TestData:
    # АДРЕС ДРАЙВЕРА
    CHROME_DRIVER_PATH = 'C:\\WebDriver\\bin\\chromedriver.exe'
    # URL личный кабинет "Ростелеком"
    START_URL = 'https://b2c.passport.rt.ru'

    # URL страниц социальных сетей
    VK_URL = 'https://oauth.vk.com/authorize?scope=login:email&state=ecp0RfPKJPMqwjTyEu6dGCpuHffFUJb6sWhwbrehVnc.ZwoVlt1xhgA.account_b2c&response_type=code&client_id=6771961&redirect_uri=https://b2c.passport.rt.ru/social/adapter/vk/auth&nonce=APjcMZM97pichG6lL9o69Q'
    OK_URL = 'https://connect.ok.ru/dk?st.cmd=OAuth2Login&st.redirect=%252Fdk%253Fst.cmd%253DOAuth2Permissions%2526amp%253Bst.scope%253Dlogin%25253Aemail%2526amp%253Bst.response_type%253Dcode%2526amp%253Bst.show_permissions%253Doff%2526amp%253Bst.redirect_uri%253Dhttps%25253A%25252F%25252Fb2c.passport.rt.ru%25252Fsocial%25252Fadapter%25252Fok%25252Fauth%2526amp%253Bst.state%253Da8pcUfq8TfL0p3Ph-VTqymqd0JLEV7T4q8SwoMNv6Q4.ZwoVlt1xhgA.account_b2c%2526amp%253Bst.client_id%253D1272957184&st.client_id=1272957184'
    MAIL_URL = 'https://connect.mail.ru/oauth/authorize?scope=login%3Aemail&state=mdNtgOHGqQwM2F0edv7qqWl0ILdFiCk4jo09fXBBDIM.ZwoVlt1xhgA.account_b2c&response_type=code&client_id=762573&redirect_uri=https://b2c.passport.rt.ru/social/adapter/mail/auth&nonce=BaOjyBNl3tAJxNbv0OfiSw'
    GOOGLE_URL = 'https://accounts.google.com/o/oauth2/auth/oauthchooseaccount?scope=openid&state=phSPXqhSch6GGbioFyEGz9d0hHLYRMxF8zPmzpYMdD4.ZwoVlt1xhgA.account_b2c&response_type=code&client_id=121868035218-rd8lrg4eb24p25g6vo6qnoerkln4b2lp.apps.googleusercontent.com&redirect_uri=https%3A%2F%2Fb2c.passport.rt.ru%2Fsocial%2Fadapter%2Fgoogle%2Fauth&nonce=jtn_gcuyT9l122qnfnRQ3Q&service=lso&flowName=GeneralOAuthFlow'
    YANDEX_URL = 'https://oauth.yandex.ru/authorize?scope=login%3Aemail&state=pqV8OG-OjoeHVDYmTIilWE3X6wkVgFuHcsmbEMjGjDI.ZwoVlt1xhgA.account_b2c&response_type=code&client_id=cca955e781554be08e4007813ddd578e&redirect_uri=https://b2c.passport.rt.ru/social/adapter/ya/auth&nonce=_n7T8xIRDBZnIzmt6H1ODg'

    # URL страницы забыл пароль
    ZABIL_PASSWORD_URL = START_URL + '/auth/realms/b2c/login-actions/reset-credentials?client_id=account_b2c&tab_id=ZwoVlt1xhgA'
    
    # URL страницы пользовательское соглашение
    USER_AGREEMENT_URL = START_URL + '/sso-static/agreement/agreement.html'
    
    # URL страницы регистрации нового пользователя
    REGISTER_URL = START_URL + '/auth/realms/b2c/login-actions/registration?client_id=account_b2c&tab_id=ZwoVlt1xhgA'
    
    
    # Параметры размера открываемой страницы на экране
    WIDTH_WINDOW_1 = 1020
    LENGTH_WINDOW_1 = 900
    WIDTH_WINDOW = 1900
    LENGTH_WINDOW = 1000

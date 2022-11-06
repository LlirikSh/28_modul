from config import TestData
from pages.locators import AuthLocators
from pages.auth_page import AuthPage
from tests.test_base import BaseTest


   def test_go_to_zabil_password(self):
      """Тест проверяет, что на главной странице сайта кнопка "Забыл пароль" переводит на страницу 'востановления пароля' """
      self.authPage = AuthPage(self.driver)
      START_FORGOT_PASSWORD = self.authPage.element_are_present(AuthLocators.AUTH_START_FORGOT_PASSWORD)
      assert START_FORGOT_PASSWORD.is_displayed(), "Элемент не виден на дисплее при ширине окна более 1020"
      self.authPage.hover_cursor_click(AuthLocators.AUTH_START_FORGOT_PASSWORD)
      # открывается страница "Отложенные", получаем URL новой страницы и сравниваем с данными из config.py
      ZABIL_PASSWORD_URL = self.authPage.get_url()
      assert ZABIL_PASSWORD_URL == TestData.ZABIL_PASSWORD_URL
 
   def test_go_to_user_agreement(self):
      """Тест проверяет, что на главной странице сайта кнопка "пользовательского соглашения" переводит на страницу 'пользовательского соглашения' """
      self.authPage = AuthPage(self.driver)
      START_USER_AGREEMENT = self.authPage.element_are_present(AuthLocators.AUTH_START_USER_AGREEMENT)
      assert START_USER_AGREEMENT.is_displayed(), "Элемент не виден на дисплее при ширине окна более 1020"
      self.authPage.hover_cursor_click(AuthLocators.AUTH_START_USER_AGREEMENT)
      # открывается страница "Отложенные", получаем URL новой страницы и сравниваем с данными из config.py
      USER_AGREEMENT_URL = self.authPage.get_url()
      assert USER_AGREEMENT_URL == TestData.USER_AGREEMENT_URL
      
    def test_go_to_forgot_password(self):
      """Тест проверяет, что на главной странице сайта кнопка "Зарегистрироваться" переводит на страницу 'регистрации нового пользователя' """
      self.authPage = AuthPage(self.driver)
      START_FORGOT_PASSWORD = self.authPage.element_are_present(AuthLocators.AUTH_START_FORGOT_PASSWORD)
      assert START_FORGOT_PASSWORD.is_displayed(), "Элемент не виден на дисплее при ширине окна более 1020"
      self.authPage.hover_cursor_click(AuthLocators.AUTH_START_FORGOT_PASSWORD)
      # открывается страница "Отложенные", получаем URL новой страницы и сравниваем с данными из config.py
      REGISTER_URL = self.authPage.get_url()
      assert REGISTER_URL == TestData.REGISTER_URL
      
   def test_go_to_vk(self):
      """Тест проверяет, что на главной странице сайта кнопка социальных сетей "ВК" переводит на страницу 'регистрация с помощью социальной сети VK' """
      self.authPage = AuthPage(self.driver)
      START_VK = self.authPage.element_are_present(AuthLocators.AUTH_START_VK)
      assert START_VK.is_displayed(), "Элемент не виден на дисплее при ширине окна более 1020"
      self.authPage.hover_cursor_click(AuthLocators.AUTH_START_VK)
      # открывается страница "Отложенные", получаем URL новой страницы и сравниваем с данными из config.py
      VK_URL = self.authPage.get_url()
      assert VK_URL == TestData.VK_URL
      
   def test_go_to_ok(self):
      """Тест проверяет, что на главной странице сайта кнопка социальных сетей "Однокласники" переводит на страницу 'регистрация с помощью социальной сети OK' """
      self.authPage = AuthPage(self.driver)
      START_OK = self.authPage.element_are_present(AuthLocators.AUTH_START_OK)
      assert START_OK.is_displayed(), "Элемент не виден на дисплее при ширине окна более 1020"
      self.authPage.hover_cursor_click(AuthLocators.AUTH_START_OK)
      # открывается страница "Отложенные", получаем URL новой страницы и сравниваем с данными из config.py
      OK_URL = self.authPage.get_url()
      assert OK_URL == TestData.OK_URL
      
   def test_go_to_my_world(self):
      """Тест проверяет, что на главной странице сайта кнопка социальных сетей "Мой мир" переводит на страницу 'регистрация с помощью социальной сети mail.ru' """
      self.authPage = AuthPage(self.driver)
      START_MY_WORLD = self.authPage.element_are_present(AuthLocators.AUTH_START_MY_WORLD)
      assert START_MY_WORLD.is_displayed(), "Элемент не виден на дисплее при ширине окна более 1020"
      self.authPage.hover_cursor_click(AuthLocators.AUTH_START_MY_WORLD)
      # открывается страница "Отложенные", получаем URL новой страницы и сравниваем с данными из config.py
      MAIL_URL = self.authPage.get_url()
      assert MAIL_URL == TestData.MAIL_URL

   def test_go_to_my_google(self):
      """Тест проверяет, что на главной странице сайта кнопка социальных сетей "Google" переводит на страницу 'регистрация с помощью социальной сети google.com' """
      self.authPage = AuthPage(self.driver)
      START_GOOGLE = self.authPage.element_are_present(AuthLocators.AUTH_START_GOOGLE)
      assert START_GOOGLE.is_displayed(), "Элемент не виден на дисплее при ширине окна более 1020"
      self.authPage.hover_cursor_click(AuthLocators.AUTH_START_GOOGLE)
      # открывается страница "Отложенные", получаем URL новой страницы и сравниваем с данными из config.py
      GOOGLE_URL = self.authPage.get_url()
      assert GOOGLE_URL == TestData.GOOGLE_URL
  
   def test_go_to_my_yandex(self):
      """Тест проверяет, что на главной странице сайта кнопка социальных сетей "Yandex" переводит на страницу 'регистрация с помощью социальной сети yandex.ru' """
      self.authPage = AuthPage(self.driver)
      START_YANDEX = self.authPage.element_are_present(AuthLocators.AUTH_START_YANDEX)
      assert START_YANDEX.is_displayed(), "Элемент не виден на дисплее при ширине окна более 1020"
      self.authPage.hover_cursor_click(AuthLocators.AUTH_START_YANDEX)
      # открывается страница "Отложенные", получаем URL новой страницы и сравниваем с данными из config.py
      YANDEX_URL = self.authPage.get_url()
      assert YANDEX_URL == TestData.YANDEX_URL


def test_go_to_page_cart(self):
      """Тест проверяет, что в шапке сайта кнопка "Корзина" переводит на страницу START_URL + '.../'"""
      self.authPage = AuthPage(self.driver)
      HEADER_BUTTON_CART = self.authPage.element_are_present(AuthLocators.AUTH_HEADER_BUTTON_CART)
      assert HEADER_BUTTON_CART.is_displayed(), "Элемент не виден на дисплее при ширине окна более 1020"
      self.authPage.hover_cursor_click(AuthLocators.AUTH_HEADER_BUTTON_CART)
      # открывается страница "Корзина", получаем URL новой страницы и сравниваем с данными из config.py
      CART_URL = self.authPage.get_url()
      assert CART_URL == TestData.CART_URL


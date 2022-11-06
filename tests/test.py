from config import TestData
from pages.locators import AuthLocators
from pages.auth_page import AuthPage
from tests.test_base import BaseTest


   def test_go_to_page_putorder(self):
      """Тест проверяет, что на главной странице сайта кнопка "Забыл пароль" переводит на страницу " востановления пароля""""
      self.authPage = AuthPage(self.driver)
      START_FORGOT_PASSWORD = self.authPage.element_are_present(AuthLocators. AUTH_START_FORGOT_PASSWORD)
      assert  START_FORGOT_PASSWORD.is_displayed(), "Элемент не виден на дисплее при ширине окна более 1020"
      self.authPage.hover_cursor_click(AuthLocators. AUTH_START_FORGOT_PASSWORD)
      # открывается страница "Отложенные", получаем URL новой страницы и сравниваем с данными из config.py
       ZABIL_PASSWORD_URL = self.authPage.get_url()
      assert  ZABIL_PASSWORD_URL == TestData. ZABIL_PASSWORD_URL


   def test_go_to_page_cart(self):
      """Тест проверяет, что в шапке сайта кнопка "Корзина" переводит на страницу START_URL + '.../'"""
      self.authPage = AuthPage(self.driver)
      HEADER_BUTTON_CART = self.authPage.element_are_present(AuthLocators.AUTH_HEADER_BUTTON_CART)
      assert HEADER_BUTTON_CART.is_displayed(), "Элемент не виден на дисплее при ширине окна более 1020"
      self.authPage.hover_cursor_click(AuthLocators.AUTH_HEADER_BUTTON_CART)
      # открывается страница "Корзина", получаем URL новой страницы и сравниваем с данными из config.py
      CART_URL = self.authPage.get_url()
      assert CART_URL == TestData.CART_URL


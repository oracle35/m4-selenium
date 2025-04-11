from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import unittest

# from util import logo


# We'll be using https://www.elimparcial.com/


class TestPaginaPrincipal(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()  # Can change it to Firefox later :)
        self.driver.get(
            "http://www.portalnoticias.com"
        )  # TODO: Change this to an actual website.

    def test_titulo_pagina(self):
        self.assertEqual(self.driver.title, "Portal de Noticias")

    def test_barra_busqueda(self):
        barra_busqueda = self.driver.find_element(By.NAME, "q")
        barra_busqueda.send_keys("clima" + Keys.RETURN)
        # Agregar comprobaciones para los resultados de búsqueda

    def tearDown(self):
        self.driver.quit()


if __name__ == "__main__":
    unittest.main()
    # print(logo.movie_logo)

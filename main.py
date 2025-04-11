from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import unittest


WEBSITE = "https://www.bbc.com/"


class TestPaginaPrincipal(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()  # Can change it to Firefox later :)
        self.driver.get(WEBSITE)  # TODO: Change this to an actual website.

    def test_titulo_pagina(self):
        self.assertEqual(self.driver.title, "BBC Home")


    def downloadPage(self):
        pass

    def tearDown(self):
        self.driver.quit()


if __name__ == "__main__":
    unittest.main()
    # print(logo.movie_logo)

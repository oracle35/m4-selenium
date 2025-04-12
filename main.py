import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import unittest


WEBSITE = "https://www.bbc.com/"


class TestPaginaPrincipal(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        # self.driver = webdriver.Firefox()  # Can change it to Firefox later :)
        self.driver.get(WEBSITE)  # TODO: Change this to an actual website.

    def test_titulo_pagina(self):
        self.assertEqual(self.driver.title, "BBC Home")


    def downloadPage(self):
        pass

    def tearDown(self):
        self.driver.quit()

class TestAccesoSecciones(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        # self.driver = webdriver.Firefox()  # Can change it to Firefox later :)
        self.driver.get(WEBSITE)  # TODO: Change this to an actual website.

    def test_acceso_news(self):
        news_button = self.driver.find_element(By.XPATH, "/html/body/div[2]/div/nav/section/nav/ul/li[2]/div/a")
        time.sleep(1)
        news_button.click()
        news_url = self.driver.current_url
        self.assertEqual(news_url, "https://www.bbc.com/news")


    def test_acceso_sport(self):
        sport_button = self.driver.find_element(By.XPATH, "/html/body/div[2]/div/nav/section/nav/ul/li[3]/div/a")
        time.sleep(1)
        sport_button.click()
        sport_url = self.driver.current_url
        self.assertEqual(sport_url, "https://www.bbc.com/sport")

        time.sleep(1)
        sport_example = self.driver.find_element(By.XPATH,"/html/body/div[2]/div/div/div[1]/div/header/div/nav/div/div[1]/div/div/div[2]/ul/li[4]/a/span")
        self.assertEqual(sport_example.text, "Formula 1")

    def test_acceso_business(self):
        business_button = self.driver.find_element(By.XPATH, "/html/body/div[2]/div/nav/section/nav/ul/li[4]/div/a")
        time.sleep(1)
        business_button.click()
        business_url = self.driver.current_url
        self.assertEqual(business_url, "https://www.bbc.com/business")

        time.sleep(1)
        business_title = self.driver.find_element(By.XPATH, "/html/body/div[2]/div/main/article/div[2]/div/div/h1")
        self.assertEqual(business_title.text, "Business")

    def test_acceso_innovation(self):
        innovation_button = self.driver.find_element(By.XPATH, "/html/body/div[2]/div/nav/section/nav/ul/li[5]/div/a")
        time.sleep(1)
        innovation_button.click()
        innovation_url = self.driver.current_url
        self.assertEqual(innovation_url, "https://www.bbc.com/innovation")

        time.sleep(1)
        business_title = self.driver.find_element(By.XPATH, "/html/body/div[2]/div/main/article/div[2]/div/div/h1")
        self.assertEqual(business_title.text, "Innovation")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()
    # print(logo.movie_logo)

import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import unittest


WEBSITE = "https://www.bbc.com/"
EXPECTED_KEYWORD = "Formula One"


class TestPaginaPrincipal(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get(WEBSITE)

    def test_titulo_pagina(self):
        self.assertEqual(
            self.driver.title,
            "BBC Home - Breaking News, World News, US News, Sports, Business, Innovation, Climate, Culture, Travel, Video & Audio",
        )  # El propia

    def tearDown(self):
        self.driver.quit()


class TestBusquedaNoticias(TestPaginaPrincipal):
    def test_busqueda_exitosa(self):
        self.driver.get(
            "https://www.bbc.com/search?q=formula+one"
        )  # Usamos Query Params para verificar que efectivamente pueda buscar dentro de la aplicación.
        element = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located(
                (By.CSS_SELECTOR, "div.sc-32f23d22-2.iumrhG")
            )
        )

        # Busca todos los divs con data-testid='newport-card'
        cards = element.find_elements(
            By.CSS_SELECTOR, "div[data-testid='newport-card']"
        )
        found = any(EXPECTED_KEYWORD.lower() in card.text.lower() for card in cards)
        self.assertTrue(
            found, f"No se encontró ninguna tarjeta que contenga '{EXPECTED_KEYWORD}'."
        )

    def test_busqueda_sin_resultados(self):
        self.driver.get("https://www.bbc.com/search?q=asldkfjalsdkjf")
        try:
            WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.TAG_NAME, "main"))
            )
            cuerpo = self.driver.find_element(By.TAG_NAME, "body").text.lower()
            self.assertIn("sorry there are no results", cuerpo)
        except Exception as e:
            self.fail(
                f"No se pudo verificar el mensaje de 'sin resultados'. Detalle: {e}"
            )


class TestPaginaArticulo(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get(WEBSITE)

    def test_abrir_articulo(self):
        first_article = self.driver.find_element(By.TAG_NAME, "h2")
        first_article_text = first_article.text
        first_article.click()

        time.sleep(1)
        article_title = self.driver.find_element(By.TAG_NAME, "h1")

        self.assertEqual(article_title.text, first_article_text)

    def test_fecha_articulo(self):
        first_article = self.driver.find_element(By.TAG_NAME, "h2")
        first_article_text = first_article.text
        first_article.click()

        time.sleep(1)
        date = len(self.driver.find_elements(By.TAG_NAME, "time")) > 0
        self.assertEqual(date, True)

    def test_info_articulo(self):
        first_article = self.driver.find_element(By.TAG_NAME, "h2")
        first_article_text = first_article.text
        first_article.click()

        time.sleep(1)
        article_info = (
            len(
                self.driver.find_elements(
                    By.XPATH, "//p[@class = 'sc-eb7bd5f6-0 fezwLZ']"
                )
            )
            > 0
        )
        self.assertEqual(article_info, True)

    def tearDown(self):
        self.driver.quit()


class TestAccesoSecciones(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get(WEBSITE)

    def test_acceso_news(self):
        wait = WebDriverWait(self.driver, 10)
        news_button = wait.until(
            EC.element_to_be_clickable(
                (By.XPATH, "//a[@data-testid='mainNavigationLink' and text()='News']") # Buscamos el botón de noticias en base al XPATH
            )
        )
        news_button.click()
        self.assertEqual(self.driver.current_url, "https://www.bbc.com/news")

    def test_acceso_sport(self):
        wait = WebDriverWait(self.driver, 10)
        sport_button = wait.until(
            EC.element_to_be_clickable(
                (By.XPATH, "//a[@data-testid='mainNavigationLink' and text()='Sport']")
            )
        )
        sport_button.click()
        self.assertEqual(self.driver.current_url, "https://www.bbc.com/sport")

        sport_example = wait.until(
            EC.presence_of_element_located((By.XPATH, "//span[text()='Formula 1']"))
        )
        self.assertEqual(sport_example.text, "Formula 1")

    def test_acceso_business(self):
        wait = WebDriverWait(self.driver, 10)

        business_button = wait.until(
            EC.element_to_be_clickable(
                (
                    By.XPATH,
                    "//a[@data-testid='mainNavigationLink' and text()='Business']",
                )
            )
        )
        business_button.click()

        business_url = self.driver.current_url
        self.assertEqual(business_url, "https://www.bbc.com/business")

        business_title = wait.until(
            EC.presence_of_element_located((By.XPATH, "//h1[text()='Business']"))
        )
        self.assertEqual(business_title.text, "Business")

    def test_acceso_innovation(self):
        wait = WebDriverWait(self.driver, 10)
        innovation_button = wait.until(
            EC.element_to_be_clickable(
                (
                    By.XPATH,
                    "//a[@data-testid='mainNavigationLink' and text()='Innovation']",
                )
            )
        )
        innovation_button.click()
        self.assertEqual(self.driver.current_url, "https://www.bbc.com/innovation")

        innovation_title = wait.until(
            EC.presence_of_element_located((By.XPATH, "//h1[text()='Innovation']"))
        )
        self.assertEqual(innovation_title.text, "Innovation")

    def tearDown(self):
        self.driver.quit()


if __name__ == "__main__":
    unittest.main()
    # print(logo.movie_logo)

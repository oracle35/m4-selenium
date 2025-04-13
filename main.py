import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

import unittest


WEBSITE = "https://www.bbc.com/"


class TestPaginaPrincipal(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get(WEBSITE)

    def test_titulo_pagina(self):
        self.assertEqual(
            self.driver.title,
            "BBC Home - Breaking News, World News, US News, Sports, Business, Innovation, Climate, Culture, Travel, Video & Audio",
        )  # Proper title of the page.

    def tearDown(self):
        self.driver.quit()


class TestBusquedaNoticias(TestPaginaPrincipal):
    def test_busqueda_exitosa(self):
        self.driver.get("https://www.bbc.com/search?q=climate+change")
        try:
            # Aumenta el tiempo de espera
            WebDriverWait(self.driver, 60).until(
                EC.presence_of_all_elements_located(
                    (By.CSS_SELECTOR, ".ssrcss-1hizfh0-PromoHeadline")
                )
            )
            resultados = self.driver.find_elements(
                By.CSS_SELECTOR, ".ssrcss-1hizfh0-PromoHeadline"
            )
            self.assertTrue(
                len(resultados) > 0,
                "No se encontraron resultados para 'climate change'",
            )
        except Exception as e:
            self.fail(
                f"No se encontraron resultados o tardaron demasiado en cargar. Detalle: {e}"
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
        # self.driver = webdriver.Firefox()  # Can change it to Firefox later :)
        self.driver.get(WEBSITE)

    def test_abrir_articulo(self):
        first_article = self.driver.find_element(By.TAG_NAME, "h2")
        first_article_text = first_article.text
        first_article.click()

        # Inside the detail page of the first article
        time.sleep(1)
        article_title = self.driver.find_element(By.TAG_NAME, "h1")

        # Assert that the article is properly linked to the detail page
        self.assertEqual(article_title.text, first_article_text)

    def test_fecha_articulo(self):
        first_article = self.driver.find_element(By.TAG_NAME, "h2")
        first_article_text = first_article.text
        first_article.click()

        # Inside the detail page of the first article
        time.sleep(1)
        # Check that the article contains a date
        date = len(self.driver.find_elements(By.TAG_NAME, "time")) > 0
        self.assertEqual(date, True)

    def test_info_articulo(self):
        first_article = self.driver.find_element(By.TAG_NAME, "h2")
        first_article_text = first_article.text
        first_article.click()

        # Inside the detail page of the first article
        time.sleep(1)
        # Check that the article contains the text with details of what happened
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
        # self.driver = webdriver.Firefox()  # Can change it to Firefox later :)
        self.driver.get(WEBSITE)

    def test_acceso_news(self):
        news_button = self.driver.find_element(
            By.XPATH, "/html/body/div[2]/div/nav/section/nav/ul/li[2]/div/a"
        )
        time.sleep(1)
        news_button.click()
        news_url = self.driver.current_url
        # Check that the news button of the main page redirects to the proper page
        self.assertEqual(news_url, "https://www.bbc.com/news")

    def test_acceso_sport(self):
        sport_button = self.driver.find_element(
            By.XPATH, "/html/body/div[2]/div/nav/section/nav/ul/li[3]/div/a"
        )
        time.sleep(1)
        sport_button.click()
        sport_url = self.driver.current_url
        # Check that the sport button in the main page redirects to the proper page
        self.assertEqual(sport_url, "https://www.bbc.com/sport")

        time.sleep(1)
        # Check that the sport page loaded properly by looking for one of the possible categories
        sport_example = self.driver.find_element(
            By.XPATH,
            "/html/body/div[2]/div/div/div[1]/div/header/div/nav/div/div[1]/div/div/div[2]/ul/li[4]/a/span",
        )
        self.assertEqual(sport_example.text, "Formula 1")

    def test_acceso_business(self):
        business_button = self.driver.find_element(
            By.XPATH, "/html/body/div[2]/div/nav/section/nav/ul/li[4]/div/a"
        )
        time.sleep(1)
        business_button.click()
        business_url = self.driver.current_url
        # Check that the business button in the main page redirects to the proper page
        self.assertEqual(business_url, "https://www.bbc.com/business")

        time.sleep(1)
        # Check that the business page loaded properly by looking for its title
        business_title = self.driver.find_element(
            By.XPATH, "/html/body/div[2]/div/main/article/div[2]/div/div/h1"
        )
        self.assertEqual(business_title.text, "Business")

    def test_acceso_innovation(self):
        innovation_button = self.driver.find_element(
            By.XPATH, "/html/body/div[2]/div/nav/section/nav/ul/li[5]/div/a"
        )
        time.sleep(1)
        innovation_button.click()
        innovation_url = self.driver.current_url
        # Check that the innovation button in the main page redirects to the proper page
        self.assertEqual(innovation_url, "https://www.bbc.com/innovation")

        time.sleep(1)
        # Check that the innovation page loaded properly by looking for it's title
        business_title = self.driver.find_element(
            By.XPATH, "/html/body/div[2]/div/main/article/div[2]/div/div/h1"
        )
        self.assertEqual(business_title.text, "Innovation")

    def tearDown(self):
        self.driver.quit()


if __name__ == "__main__":
    unittest.main()
    # print(logo.movie_logo)

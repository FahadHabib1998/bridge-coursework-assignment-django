from django.test import TestCase
from selenium import webdriver
from selenium.webdriver import ActionChains

# Create your tests here.
class FunctionalTests(TestCase):

    def setUp(self):
        self.browser = webdriver.Firefox(executable_path=r'/Users/fahadhabibalwaheedi/Desktop/University/SecondYear/BridgeCourseWork/brdgassign/myvenv/bin/geckodriver')

    def test_cvpage_url(self):
        self.browser.get('http://localhost:8000/cv')
        self.assertIn('Welcome to CV',self.browser.page_source)

    def test_mainpage_button_redirect(self):
        print("hello")
        self.browser.get('http://localhost:8000')
        cv_button = self.browser.find_elements_by_xpath("/html/body/center/div[2]/button[2]/a").click()
        self.assertIn('http://localhost:8000/cv',self.browser.current_url)

    def tearDown(self):
        self.browser.quit()

import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys


class demo(unittest.TestCase):

        def setUp(self):
            self.driver = webdriver.Chrome()

        def test_search_in_python_org(self):
            self.driver = webdriver.Chrome()
            self.driver.get('http://python.org')
            assert 'Python' in self.driver.title
            elem = self.driver.find_element_by_name("q")
            elem.send_keys("pycon")
            elem.send_keys(Keys.RETURN)
            assert "No results found." not in self.driver.page_source

        def tearDown(self):
            self.driver.close()

        if __name__ == "__main__":
            unittest.main()

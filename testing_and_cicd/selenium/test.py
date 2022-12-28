from lib2to3.pgen2 import driver
from selenium import webdriver
import os
import pathlib
import unittest


def file_uri(filename):
    return pathlib.Path(os.path.abspath(filename)).as_uri()

driver = webdriver.Chrome()

class WebPageTests(unittest.TestCase):

    def test_title(self):
        driver.get(file_uri("counter.html"))
        self.assertEqual(driver.title,"Counter")
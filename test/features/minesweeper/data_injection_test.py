import unittest
from hamcrest import assert_that, is_
from nose.plugins.attrib import attr
from nose.tools import istest
import requests
from testconfig import config
from splinter import Browser

from selenium import webdriver

@attr(needs_server=True)
class DataInjectionChallengeFeatureTest(unittest.TestCase):

    def setUp(self):
        import logging
        selenium_logger = logging.getLogger('selenium.webdriver.remote.remote_connection')
        selenium_logger.setLevel(logging.WARNING)
        self.browser = webdriver.Firefox()
        self.addCleanup(self.browser.quit)

    @istest
    def is_possible(self):        
        self.browser.get(config['server_url'] + '/minesweeper')
        self.browser.execute_script('document.grid=[["empty", "bomb"]]')
        self.browser.execute_script('load()')
        cell = self.browser.find_element_by_id('cell-1x2')
        cell.click()

        assert_that(self.browser.find_element_by_id('cell-1x2').get_attribute('class'), is_('lost'))
            

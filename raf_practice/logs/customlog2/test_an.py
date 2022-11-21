import logging
import pytest
import raf_practice.logs.customolog.custom_logger as cl
import pytest
from selenium import webdriver

from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen


class Test_001_Login:
    log = cl.customLogger(logging.DEBUG)

    def test_homePageTitle(self):
        self.log.debug('debug message')
        self.log.info('info message')
        self.log.warning('warn message')
        self.log.error('error message')
        self.log.critical('critical message')

    def test_login(self):
        self.log.debug('debug message')
        self.log.info('info message')
        self.log.warning('warn message')
        self.log.error('error message')
        self.log.critical('critical message')

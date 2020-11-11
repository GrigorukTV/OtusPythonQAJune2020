import argparse
from selenium import webdriver
from selenium.webdriver import ChromeOptions, FirefoxOptions
from webdrivermanager import ChromeDriverManager, GeckoDriverManager



parser = argparse.ArgumentParser()


parser.add_argument('--browser',
                    help='Введите тип браузера',
                    choices=['chrome', 'firefox'])
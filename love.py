# -*- coding: utf-8 -*-

# @author: jwx

from selenium import webdriver
from selenium.webdriver.common.keys import keys
import time

class love():
    def __init__(self):
        self.id_number = input('your id is: ')
        print('your id number is: {}'.format(self.id_number))

        self.password = input('your password is: ')
        print('your password is: {}.format(self.keyword)')

        print('if you are a graduate student, please input 1')
        print('if you are an undergraduate, please input 2')
        print('if you are a teacher, please input 3')
        print('if you are other identity, please input 4')
        self.value = input('please input: ')

        print("webdriver's path is like: 'D:/cs/python/chromedriver.exe'")
        self.path = input("please input your webdriver's path: ")
        self.driver = webdriver.Chrome(self.path)

        self.equipment = input("the equipment you want to order: ")

    def please_wait(self):
        self.wait_time = int(input('time you want to wait: '))
        time.sleep(self.wait_time)

    def deal(self):

# -*- coding: utf-8 -*-

import os
import re
import sys
import glob
import time
import random
import requests
import datetime
import urllib.request
from time import sleep
from bs4 import BeautifulSoup
from datetime import datetime
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

SESS_DIR = '/Users/username/Crawling/facebook_click_like/chromedriver_sess/'
chrome_driver = '/Users/username/Crawling/facebook_click_like/chromedriver'

UID = 'USERID'
PWD = 'PASSWORD'

SNUM = 8
ENUM = 16

class Facebook:

	def __init__(self,cnt):
		self.cnt = cnt

	def set_params(self):
		self.cnt = sys.argv[1]

	def validate(self):
		default	= {
			'cnt':'10'
		}

		self.cnt = default.get('cnt') if self.cnt == '' else self.cnt


	def like_feed(self,number,driver):
		
		try:
			if number > 0: 
				sleep(random.randint(SNUM,ENUM))
		
				for i in range(0,number):
					print('loop: [{}]'.format(i))
					print(1)

					try:
						print('case1')
						print(2)
						like_action = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '/html/body/div/div/div[4]/div/div/div[4]/div/div[2]/section/article/footer/div/div[2]/div/a'))) 
						print(3)
						like_path = driver.find_element_by_xpath('html/body/div/div/div[4]/div/div/div[4]/div/div[2]/section/article/footer/div/div[2]/div/a')
						print(4)
						like_state = like_path.get_attribute('aria-pressed')
						print(like_state) 
						print(5)
						if like_state == 'false': 
							print('Click because you donot like it') 
							like_action.click() 
						else: 
							print('Liked')
						sleep(random.randint(SNUM,ENUM))
					except:
						pass

					try:
						print('case2')
						print(2)
						like_action = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '/html/body/div/div/div[4]/div/div/div[5]/div/div[2]/section/article/footer/div/div[2]/div/a'))) 
						print(3)
						like_path = driver.find_element_by_xpath('html/body/div/div/div[4]/div/div/div[5]/div/div[2]/section/article/footer/div/div[2]/div/a')
						print(4)
						like_state = like_path.get_attribute('aria-pressed')
						print(like_state) 
						print(5)
						if like_state == 'false': 
							print('Click because you donot like it') 
							like_action.click() 
						else: 
							print('Liked')
						sleep(random.randint(SNUM,ENUM))
					except:
						pass	

					try:
						print('case3')
						print(2)
						like_action = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '/html/body/div/div/div[4]/div/div/div[6]/div/div[2]/section/article/footer/div/div[2]/div/a'))) 
						print(3)
						like_path = driver.find_element_by_xpath('html/body/div/div/div[4]/div/div/div[6]/div/div[2]/section/article/footer/div/div[2]/div/a')
						print(4)
						like_state = like_path.get_attribute('aria-pressed')
						print(like_state) 
						print(5)
						if like_state == 'false': 
							print('Click because you donot like it') 
							like_action.click() 
						else: 
							print('Liked')
						sleep(random.randint(SNUM,ENUM))
					except:
						pass					

					driver.refresh()

		except Exception as e:
			with open('./error.log','a') as file:
				file.write('You got an error: {}\n'.format(str(e)))

	def login(self):
		chrome_options = Options()
		chrome_options.add_argument('--user-agent=Mozilla/5.0 (iPhone; CPU iPhone OS 10_3 like Mac OS X) AppleWebKit/602.1.50 (KHTML, like Gecko) CriOS/56.0.2924.75 Mobile/14E5239e Safari/602.1')
		mobile_emulation = { "deviceName": "iPhone 6 Plus" }
		chrome_options.add_experimental_option("mobileEmulation", mobile_emulation)
		chrome_options.add_argument('--window-size=640,960')
		chrome_options.add_experimental_option("excludeSwitches", ["enable-logging"])
		chrome_options.add_argument('--user-data-dir={}'.format(SESS_DIR))

		driver = webdriver.Chrome(chrome_driver,options=chrome_options)

		driver.get('https://www.facebook.com') 

		#sleep(600)
		sleep(random.randint(SNUM,ENUM))

		try:
			element = driver.find_element_by_xpath("//button[@class='_54k8 _52jh _56bs _56b_ _28lf _9cow _56bw _56bu']").text
		except:
			element = ''		

		if element == '로그인':
			print('none session')
			driver.find_element_by_name('email').send_keys(UID)
			driver.find_element_by_name('pass').send_keys(PWD)
			driver.find_element_by_name('login').click()
			sleep(random.randint(SNUM,ENUM))
			self.like_feed(int(self.cnt),driver)
		else:
			print('exist session')
			sleep(random.randint(SNUM,ENUM))
			#sleep(1200)
			self.like_feed(int(self.cnt),driver)


		sleep(random.randint(SNUM,ENUM))
		driver.quit()    		

	def execute(self):

		self.validate()

		print('start')

		try:
			self.login()
		except Exception as e:
			with open('./error.log','a') as file:
				file.write('You got an error: {}\n'.format(str(e)))

		print('end')

def run():
	facebook = Facebook('')
	facebook.set_params()
	facebook.execute()

if __name__ == "__main__":
	run()
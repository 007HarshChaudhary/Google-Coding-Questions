# -*- coding: utf-8 -*-
"""
Created on Wed Jun  3 16:56:00 2020

@author: Harsh Chaudhary
"""
import time
from selenium import webdriver
views = 70
view_time = 4.5*60


browser = webdriver.Chrome()

for i in range(views):
    browser.get('https://youtu.be/aGRu-gYdgJM')
    time.sleep(view_time)

browser.close()
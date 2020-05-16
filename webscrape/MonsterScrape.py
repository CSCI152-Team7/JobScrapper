#!/usr/bin/env python
# coding: utf-8

# In[3]:


from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
import pandas as pd
import numpy as np
import random
import time

browser = webdriver.Firefox()
browser.get("https://www.monster.com/jobs/search/?q=Computer-Science&where=Fresno__2C-CA&intcid=skr_navigation_nhpso_searchMain")


# In[5]:


description = []
place = []
title = browser.find_elements_by_css_selector('h2.title')
print(title)


# In[12]:


#code works, it tries to get the description of each job on the Monster website.
#When it reaches to a certain point of going through all the job postings, the
#code stops working.
#rand = random.randrange(2,7)
#for i in range(len(title)):
    #title[i].click()
    #time.sleep(rand)
    #try:
        #temp = browser.find_elements_by_css_selector('#vjs-desc')
        #location = browser.find_elements_by_css_selector('#vjs-loc')
        #for j in temp:
            #j = j.get_attribute('innerHTML')
            #description.append(j)
            #print(j)
        #for i in location:
            #i = i.get_attribute('innerHTML')
            #place.append(i)
    #except NoSuchElementException:
        #description.append(" ")
        #place.append(" ")


# In[ ]:





# In[ ]:





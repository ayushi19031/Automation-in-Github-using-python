
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from github import GithubObject
import time
import os
browser = webdriver.Chrome(executable_path= r"C:\Users\ayush\Downloads\chromedriver_win32\chromedriver.exe")
x = browser.get('https://github.com/')
sign_in_1 = browser.find_element_by_xpath("/html/body/div[1]/header/div/div[2]/div[2]/a[1]")
actions = ActionChains(browser)
actions.click(sign_in_1).perform()
username = browser.find_element_by_xpath('//*[@id="login_field"]')
username.send_keys("ayushi19031")
password = browser.find_element_by_xpath('//*[@id="password"]')
password.send_keys("ayushij27")
sign_in_2 = browser.find_element_by_xpath('//*[@id="login"]/form/div[4]/input[9]')
actions = ActionChains(browser)
actions.click(sign_in_2).perform()

ACCESS_TOKEN = '0870c0ff1c5d2e57d3b25500fe7a2fd1c12398a8'
g = GithubObject(ACCESS_TOKEN)
print(g.get_user().get_repos())

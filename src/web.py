from selenium import webdriver
from time import sleep

options = webdriver.ChromeOptions()
options.add_argument('--ignore-certificate-errors')
driver = webdriver.Chrome('/usr/local/bin/chromedriver')
driver.get('https://mytree.itreetools.org/#/')
sleep(5)

address = driver.find_element_by_xpath('//*[@id="address"]')
address.clear()
address.send_keys('106 Gaskin Avenue Gambier, Ohio 43022')
submit_button = driver.find_element_by_xpath('//*[@id="content"]/div/div[7]/div/a/button')
submit_button.click()
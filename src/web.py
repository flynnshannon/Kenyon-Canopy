from selenium import webdriver
from time import sleep

def fill_from_xpath(driver, xpath, content):
  field = driver.find_element_by_xpath(xpath)
  field.clear()
  field.send_keys(content)

def click(driver, xpath):
  button = driver.find_element_by_xpath(xpath)
  button.click()

options = webdriver.ChromeOptions()
options.add_argument('--ignore-certificate-errors')
driver = webdriver.Chrome('/usr/local/bin/chromedriver')
driver.get('https://mytree.itreetools.org/#/')
sleep(5)

fill_from_xpath(driver, '//*[@id="address"]', '106 Gaskin Avenue Gambier, Ohio 43022')
click(driver, '//*[@id="content"]/div/div[7]/div/a/button')


'''address = driver.find_element_by_xpath('//*[@id="address"]')
address.clear()
address.send_keys('106 Gaskin Avenue Gambier, Ohio 43022')
submit_button = driver.find_element_by_xpath('//*[@id="content"]/div/div[7]/div/a/button')
submit_button.click()'''
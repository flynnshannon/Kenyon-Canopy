from selenium import webdriver
from selenium.webdriver.support.ui import Select
from time import sleep

def fill_from_xpath(driver, xpath, content):
  field = driver.find_element_by_xpath(xpath)
  field.clear()
  field.send_keys(content)

def fill_dropdown(driver, dropdown_xpath, selection_xpath):
  click(driver, dropdown_xpath)
  click(driver, selection_xpath)

def click(driver, xpath):
  driver.find_element_by_xpath(xpath).click()

options = webdriver.ChromeOptions()
options.add_argument('--ignore-certificate-errors')
driver = webdriver.Chrome('/usr/local/bin/chromedriver')
driver.get('https://mytree.itreetools.org/#/')
sleep(5)

#address
fill_from_xpath(driver, '//*[@id="address"]', '106 Gaskin Avenue Gambier, Ohio 43022')
#go to next page
click(driver, '//*[@id="content"]/div/div[7]/div/a/button')
#wait for page to load
sleep(5)

#need to think more about how to add species
#iTree-Tools requires you to start typing then selected
#maybe we do a dropdown of trees Dave identifies as being on campus in the Google formaH

#TODO:
  #add function for filling from dropdown

#species
fill_from_xpath(driver, '//*[@id="species-input"]', 'red maple')
click(driver, '//*[@id="species-option-container"]/span[7]')

#diameter in inches
fill_from_xpath(driver, '//*[@id="diameter"]', '20.4')

#tree condition
fill_dropdown(driver, '//*[@id="condition"]', '//*[@id="condition"]/option[2]')

#sun exposure
fill_dropdown(driver, '//*[@id="exposure"]', '//*[@id="exposure"]/option[2]')

click(driver, '//*[@id="content"]/form/div/div[10]/div[2]/a/button')
sleep(2)

#this will be read from sheet
near_building = True

if near_building:
  #building year
  fill_dropdown(driver, '//*[@id="vintage"]', '//*[@id="vintage"]/option[2]')

  #distance from building
  fill_dropdown(driver, '//*[@id="distance"]', '//*[@id="distance"]/option[2]')

  #direction from tree to near_building
  fill_dropdown(driver, '//*[@id="direction"]', '//*[@id="direction"]/option[2]')
click(driver, '//*[@id="content"]/form/div[3]/div[1]/div[2]/a/button')
sleep(5)

#calculate benefits
click(driver, '//*[@id="view"]')
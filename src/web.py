from selenium import webdriver
from time import sleep

def fill_from_xpath(driver, xpath, content):
  field = driver.find_element_by_xpath(xpath)
  field.clear()
  field.send_keys(content)

def fill_dropdown(driver, xpath, content):
  pass

def click(driver, xpath):
  button = driver.find_element_by_xpath(xpath)
  button.click()

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

#diameter in inches
fill_from_xpath(driver, '//*[@id="diameter"]', '20.4')

#tree condition
fill_dropdown(driver, '//*[@id="condition"]', 'Good')

#sun exposure
fill_dropdown(driver, '//*[@id="exposure"]', 'Full')

click(driver, '//*[@id="content"]/form/div/div[10]/div[2]/a/button')
sleep(5)

#this will be read from sheet
near_building = False

if near_building:
  #building year
  fill_dropdown(driver, '//*[@id="vintage"]', 'Before 1980')

  #distance from building
  fill_dropdown(driver, '//*[@id="distance"]', '>60')

  #direction from tree to near_building
  fill_dropdown(driver, '//*[@id="direction"]', 'north')
click(driver, '//*[@id="content"]/form/div[3]/div[1]/div[2]/a/button')
sleep(5)

#calculate benefits
click(driver, '//*[@id="view"]/span/svg/path')

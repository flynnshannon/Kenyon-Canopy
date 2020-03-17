from selenium import webdriver
from selenium.webdriver.support.ui import Select
from time import sleep
from tree import Tree

#TODO: create dictionaries for xpath for dropdowns
#or do this in tree.py (probably cleaner)

def fill_from_xpath(driver, xpath, content):
  field = driver.find_element_by_xpath(xpath)
  field.clear()
  field.send_keys(content)

def fill_dropdown(driver, dropdown_xpath, selection_xpath):
  click(driver, dropdown_xpath)
  click(driver, selection_xpath)

def click(driver, xpath):
  driver.find_element_by_xpath(xpath).click()

def enter_tree(my_tree):
  options = webdriver.ChromeOptions()
  options.add_argument('--ignore-certificate-errors')
  driver = webdriver.Chrome('/usr/local/bin/chromedriver')
  driver.get('https://mytree.itreetools.org/#/')
  sleep(5)

  #address
  fill_from_xpath(driver, '//*[@id="address"]', my_tree.address)
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
  fill_from_xpath(driver, '//*[@id="species-input"]', my_tree.species[0])
  click(driver, my_tree.species[1])

  #diameter in inches
  fill_from_xpath(driver, '//*[@id="diameter"]', my_tree.diam)

  #tree condition
  fill_dropdown(driver, '//*[@id="condition"]', my_tree.condition)

  #sun exposure
  fill_dropdown(driver, '//*[@id="exposure"]', my_tree.exposure)

  click(driver, '//*[@id="content"]/form/div/div[10]/div[2]/a/button')
  sleep(2)

  if my_tree.near_building:
    #building year
    fill_dropdown(driver, '//*[@id="vintage"]', my_tree.building_year)

    #distance from building
    fill_dropdown(driver, '//*[@id="distance"]', my_tree.distance_to_building)

    #direction from tree to near_building
    fill_dropdown(driver, '//*[@id="direction"]', my_tree.direction_to_building)
  click(driver, '//*[@id="content"]/form/div[3]/div[1]/div[2]/a/button')
  sleep(5)

  #calculate benefits
  click(driver, '//*[@id="view"]')


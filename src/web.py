from selenium import webdriver
from selenium.webdriver.support.ui import Select
from time import sleep
from tree import Tree

# TODO: create dictionaries for xpath for dropdowns
# or do this in tree.py (probably cleaner)


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
  driver.get('https://mytree.itreetools.org/#/location')
  sleep(5)

  # address
  fill_from_xpath(driver, '//*[@id="addressInput"]', my_tree.address)
  # go to next page
  click(driver, '//*[@id="content"]/div/div[4]/div[3]/a/button')
  # wait for page to load
  sleep(10)

  # need to think more about how to add species
  # iTree-Tools requires you to start typing then selected
  # maybe we do a dropdown of trees Dave identifies as being on campus in the Google formaH

  # species
  click(driver, '//*[@id="species-input"]')
  fill_from_xpath(driver, '//*[@id="species-input"]', my_tree.species[0])
  # driver.select_by_visible_text(my_tree.species[0])
  click(driver, my_tree.species[1])

  #diameter in inches
  fill_from_xpath(driver, '//*[@id="diameter"]', my_tree.diam)

  # tree condition
  fill_dropdown(driver, '//*[@id="condition"]', my_tree.condition)

  # sun exposure
  click(driver, my_tree.exposure)

  if my_tree.near_building:
    click(driver, '//*[@id="proximity"]/button[1]')
    sleep(2)
    # building year
    print(my_tree.building_year)
    fill_dropdown(driver, '//*[@id="vintage"]', my_tree.building_year)

    # distance from building
    fill_dropdown(driver, '//*[@id="distance"]', my_tree.distance_to_building)

    # direction from tree to near_building
    fill_dropdown(driver, '//*[@id="direction"]',
                  my_tree.direction_to_building)
  else:
    click(driver, '//*[@id="proximity"]/button[2]')
  click(driver, '//*[@id="content"]/form/div/div[16]/div/a/button/span')
  sleep(5)

  # calculate benefits
  click(driver, '//*[@id="content"]/div/div[2]/div[2]/a/button')
  click(driver, 'force an error to occur to prevent window from closing during testing')

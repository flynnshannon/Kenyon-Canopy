from selenium import webdriver
from selenium.webdriver.support.ui import Select
from time import sleep
from tree import Tree

# TODO: create dictionaries for xpath for dropdowns
# or do this in tree.py (probably cleaner)

total_benefit = '//*[@id="nutrition"]/div[5]/div/span'
carbon_sequestered_dollars = '//*[@id="nutrition"]/div[7]/div/div[1]/strong/span'
carbon_stored_lbs = '//*[@id="nutrition"]/div[7]/div/div[2]/span'
storm_water_dollars = '//*[@id="nutrition"]/div[8]/div/div[1]/strong/span'
rainfall_gal = '//*[@id="nutrition"]/div[8]/div/div[3]/span'
air_pollution_removed = '//*[@id="nutrition"]/div[9]/div/div[1]/strong/span'


def fill_from_xpath(driver, xpath, content):
  field = driver.find_element_by_xpath(xpath)
  field.clear()
  #field.click()
  field.send_keys(content)


def fill_dropdown(driver, dropdown_xpath, selection_xpath):
  click(driver, dropdown_xpath)
  click(driver, selection_xpath)


def click(driver, xpath):
  driver.find_element_by_xpath(xpath).click()

def enter_tree(my_tree, driver):
  # address
  fill_from_xpath(driver, '//*[@id="addressInput"]', my_tree.address)
  # go to next page
  click(driver, '//*[@id="content"]/div/div[4]/div[3]/a/button')
  # wait for page to load
  sleep(5)

  # need to think more about how to add species
  # iTree-Tools requires you to start typing then selected
  # maybe we do a dropdown of trees Dave identifies as being on campus in the Google formaH

  # species
  click(driver, '//*[@id="species-input"]')
  fill_from_xpath(driver, '//*[@id="species-input"]', my_tree.species[0])
  sleep(3)

  click(driver, my_tree.species[1])

  # diameter in inches
  fill_from_xpath(driver, '//*[@id="diameter"]', my_tree.diam)

  # tree condition
  #needs to accept more types
  fill_dropdown(driver, '//*[@id="condition"]', '//*[@id="condition"]/option[2]')

  # sun exposure
  #needs to accept more types
  click(driver, '//*[@id="exposure"]/button[3]')

  if my_tree.near_building:
    click(driver, '//*[@id="proximity"]/button[1]')
    sleep(2)
    # building year
    print(my_tree.building_year)
    #needs to accept more types
    fill_dropdown(driver, '//*[@id="vintage"]', '//*[@id="vintage"]/option[3]')

    # distance from building
    #needs to accept more types
    fill_dropdown(driver, '//*[@id="distance"]', '//*[@id="distance"]/option[2]')

    # direction from tree to near_building
    #needs to accpet more types
    fill_dropdown(driver, '//*[@id="direction"]',
                  '//*[@id="direction"]/option[2]')
  else:
    click(driver, '//*[@id="proximity"]/button[2]')
  click(driver, '//*[@id="content"]/form/div/div[16]/div/a/button/span')
  sleep(2)
  click(driver, '//*[@id="content"]/div/div[2]/div[2]/a/button')

  print('Total benefit: ' + driver.find_element_by_xpath(total_benefit).text)
  print('Carbon sequestered ($): ' +
        driver.find_element_by_xpath(carbon_sequestered_dollars).text)
  print('Carbon stored (lbs): ' +
        driver.find_element_by_xpath(carbon_stored_lbs).text)
  print('Storm water runnoff avoided ($): ' +
        driver.find_element_by_xpath(storm_water_dollars).text)
  print('Rainfall intercepted (gal): ' +
        driver.find_element_by_xpath(rainfall_gal).text)
  print('Air pollution removed ($): ' +
        driver.find_element_by_xpath(air_pollution_removed).text)

  return [driver.find_element_by_xpath(total_benefit).text, driver.find_element_by_xpath(carbon_sequestered_dollars).text, driver.find_element_by_xpath(carbon_stored_lbs).text, driver.find_element_by_xpath(storm_water_dollars).text, driver.find_element_by_xpath(rainfall_gal).text, driver.find_element_by_xpath(air_pollution_removed).text]

def get_forest_metrics(forest):
    metrics = []
    options = webdriver.ChromeOptions()
    options.add_argument('--ignore-certificate-errors')
    #comment out the line below to see chrome
    # options.add_argument('headless')
    driver = webdriver.Chrome('/usr/local/bin/chromedriver', chrome_options=options)
    driver.get('https://mytree.itreetools.org/#/location')
    sleep(2)
    for i in range(len(forest)):
        metrics.append(enter_tree(forest[i], driver))
        if i < len(forest) - 1:
            click(driver,'//*[@id="content"]/div[1]/a/button')
            sleep(3)
            click(driver, '//*[@id="delete"]')
            sleep(2)
            click(driver, '//*[@id="content"]/div/div[2]/div[1]/a/button')
            sleep(3)
    return metrics

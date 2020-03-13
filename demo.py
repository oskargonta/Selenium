from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import select
from selenium.webdriver.support.select import Select
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome (r'C:\Users\gonta\PycharmProjects\Selenium\seleniumddemo\chromedriver.exe')
driver.implicitly_wait(10)
driver.maximize_window ()
driver.get ('https://www.getakite.de')

driver.find_element_by_id('show_advanced_searchform').click()
driver.implicitly_wait(10)

driver.find_element_by_id('id_category').click()
driver.implicitly_wait(20)
po_id = Select(driver.find_element_by_id('id_category'))
po_id.select_by_value('1')

driver.find_element_by_id("id_keyword").click()
driver.find_element_by_id("id_keyword").clear()
driver.find_element_by_id("id_keyword").send_keys('Soul')

driver.find_element_by_id('id_factory').click()
company_name_select = Select(driver.find_element_by_id('id_factory'))
company_name_select.select_by_visible_text('Flysurfer')

print("cos tam ")

driver.find_element_by_id('id_price_0').send_keys('1000')
driver.find_element_by_id('id_price_1').send_keys('1800')

year_pre_prod_select = Select(driver.find_element_by_id('id_year_0'))
year_pre_prod_select.select_by_value('18')

year_post_prod_select = Select(driver.find_element_by_id('id_year_1'))
year_post_prod_select.select_by_value('21')

from_kite_size = Select(driver.find_element_by_id('id_kitesize_0'))
from_kite_size.select_by_value('34')

to_kite_size = Select(driver.find_element_by_id('id_kitesize_1'))
to_kite_size.select_by_value('37')

submit_button = driver.find_element_by_xpath ( "//button[@type='submit']" ).click ()
driver.implicitly_wait(10)



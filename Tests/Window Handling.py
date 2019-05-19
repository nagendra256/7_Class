from selenium import webdriver
import time
driver=webdriver.Chrome()
driver.get("http://citibank.co.in")
driver.maximize_window()
driver.implicitly_wait(20)
driver.delete_all_cookies()
current_window_id=driver.current_window_handle
print(current_window_id)
time.sleep(10)
driver.find_element_by_xpath("//a[@title='Login']").click()
window_ids=driver.window_handles
print(type(window_ids))
print(window_ids)
for handle in window_ids:
    print(handle)
    if handle !=current_window_id:
        driver.switch_to.window(handle)
        driver.find_element_by_xpath("//input[@id='User_Id']").send_keys('Dummyuser')
driver.quit()

from selenium import webdriver

driver=webdriver.Chrome()
driver.get("file:///C:/Users/nagen/Desktop/WebTable.html")
driver.maximize_window()
driver.implicitly_wait(30)

row_length=driver.find_elements_by_xpath("//*[@id='emp']/tbody/tr")
print(len(row_length))
column_length=driver.find_elements_by_xpath("//*[@id='emp']/thead/tr/th")
print(len(column_length))
first_part="//*[@id='emp']/thead/tr/th["
second_part="]"


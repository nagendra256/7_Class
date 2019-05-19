from selenium import webdriver

driver=webdriver.Chrome()
driver.get("file:///C:/Users/nagen/Desktop/WebTable.html")
driver.maximize_window()
driver.implicitly_wait(30)

row_length=driver.find_elements_by_xpath("//*[@id='emp']/tbody/tr")
print('row length is',len(row_length))
column_length=driver.find_elements_by_xpath("//*[@id='emp']/thead/tr/th")
print('column legnth is',len(column_length))
header_data=driver.find_elements_by_xpath("//*[@id='emp']/thead/tr/th")
print('header count is',len(header_data))
for data in header_data:
    result=data
    print(result.text)
'''second row data'''

table_data=driver.find_elements_by_xpath("//*[@id='emp']")
print('-----Entire Table Data------')
for data in table_data:
    result=data
    print(result.text)


first_column=driver.find_elements_by_xpath("//tr/td[1]")
for data in first_column:
    result=data
    print('First Column data',result.text)
third_column=driver.find_elements_by_xpath("//tr/td[3]")
for data in third_column:
    result=data
    print('Third Column data',result.text)
'''to check if the employee in the second row is getting correct salary mentioned in the table'''
first_part="//*[@id='emp']/tbody/tr[1]"
second_part="/td["
third_part="]"
for i in column_length:
    res=i
    print(res.text)
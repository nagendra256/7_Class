from selenium import webdriver
browser='ie'
if browser=='chrome':
    driver= webdriver.Chrome()
    driver.get("http://sc.com/in")
elif browser=='firefox':
    driver= webdriver.Firefox()
    driver.get("http://sc.com/in")
elif browser=='ie':
    driver= webdriver.Ie()
    driver.get("http://sc.com/in")
else:
    print("enter valid browser name")

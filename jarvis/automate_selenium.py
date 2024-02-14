import selenium
from selenium import webdriver
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By

import time

driver=webdriver.Chrome(executable_path="C:\\Users\\DELL\\Documents\\webdrivers\\chromedriver_win32\\chromedriver.exe")
driver.get("http://ngitonline.com/login/index.php")
driver.maximize_window() #will maximize the page
# print(driver.title)  #captures the tittle of page
# print(driver.current_url)  #prints present url
# print(driver.page_source) #Returns the page HTML
driver.implicitly_wait(5) #this function is used to stop the execution of programme for the specified time in seconds , when an element is not still loaded , if it is already loaded then this will not wait , this function should be used only once in a programme block as this will be applicable to all the elements

#ele_link=driver.find_element_by_xpath("//*[@id='region-main']/div/div/div[1]/table/tbody/tr[2]/td[3]/a").click()


ele_user=driver.find_element_by_xpath("//*[@id='username']")  # or ele_user=driver.find_element_by_name("username") or ele_user=driver.find_element(By.ID,"id should be entered here")
print(ele_user.is_displayed()) # checks whether displayed if displayed returns true else false
print(ele_user.is_enabled())  # checks whether enabled or not , if enabled returns true else returns false

ele_user.send_keys("20BD1A055T") #  sends the text inside and fills it

ele_pass=driver.find_element_by_name("password")
ele_pass.send_keys("8309882962@")

ele_login=driver.find_element_by_xpath("//*[@id='loginbtn']").click()



'''
# waits till max time specified ,here it is 10 sec . and EC.condition # should import : from selenium.webdriver.support.ui import WebDriverWait and from selenium.webdriver.common.by import By and from selenium.webdriver.support import expected_conditions as EC
wait=WebDriverWait(driver,10)
eleee=wait.until(EC.element_to_be_clickable(By.XPATH,""))
'''
'''
driver.find_element_by_name("password").clear() # This will clear the text in the password
'''
'''
css_selelkflibi=driver.find_element_by_css_selector("tag[atrribute=value]")
'''
'''
 el.is_selected()  #is used to check whether a radio button is checked or not
 
'''

'''
driver.find_element_by_xpath("//*[@id='login']/div[3]/a").click()  #copy the elements xpath from inspect - copy - copy xpath , now remove double quotes and replace with single quotes # In this click is used to say it should be clicked
time.sleep(2)
'''

'''
driver.back() #will take a page back
time.sleep(2)
driver.forward() #will take a page forward
time.sleep(2)
'''


#driver.close() #close the browsers one window the one which we opened at first
#driver.quit() #closes all the browsers

from logging import currentframe
from selenium import webdriver
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as Ec
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.chrome.options import Options  #For using detach option
from selenium.webdriver import ChromeOptions, Chrome
import time

def to():
        # if ("open" and "tessellator") in query: #KMIT
                # speak("opening")
                driver=webdriver.Chrome(executable_path='C:\\Users\\DELL\\Documents\\webdrivers\\chromedriver_win32\\chromedriver.exe')
                driver.maximize_window() #will maximize the page
                driver.implicitly_wait(5) #this function is used to stop the execution of programme for the specified time in seconds , when an element is not still loaded , if it is already loaded then this will not wait , this function should be used only once in a programme block as this will be applicable to all the elements
                driver.get("http://kmitonline.com/login/index.php")
                ele_user=driver.find_element_by_xpath("//*[@id='username']")  # or ele=driver.find_element_by_name("username")
                ele_user.send_keys("20BD1A055T") #  sends the text inside and fills it

                ele_pass=driver.find_element_by_name("password")
                ele_pass.send_keys("Kmit123$")

                ele_login=driver.find_element_by_xpath("//*[@id='loginbtn']").click()
                driver.implicitly_wait(50000)

                ele_join=driver.find_element_by_xpath("//*[@id='region-main']/div/div/div/div/div[3]/a/span").click()
                Options().add_experimental_option("detach",True)
                time.sleep(500)
                # speak("opened")
                # to()

to()
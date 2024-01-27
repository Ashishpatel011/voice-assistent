from selenium import webdriver
from selenium.webdriver.common.by import By
class infow():
    def __init__(self):
        self.driver=webdriver.Chrome(executable_path="C:\Program Files\Google\chromedriver_win32[1]\chromedriver.exe")

    def get_info(self,query):
        self.query=query
        self.driver.get(url="https://www.wikipedia.org")
        search=self.driver.find_element(By.XPATH,'//*[@id="searchInput"]')
        search.click()
        search.send_keys(query)
        enter=self.driver.find_element(By.XPATH,'//*[@id="search-form"]/fieldset/button/i')
        enter.click() 
        
        while (True) :
            continue           
#assist=infow()  
# assist.get_info('cricket')
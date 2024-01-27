from selenium import webdriver
from selenium.webdriver.common.by import By
class music():
    def __init__(self):
        self.driver=webdriver.Chrome(executable_path="C:\Program Files\Google\chromedriver_win32[1]\chromedriver.exe")
    
    def play(self,query):
        self.query=query
        self.driver.get(url="https://www.youtube.com/results?search_query="+query)
        video=self.driver.find_element(By.XPATH,'//*[@id="dismissible"]')
        video.click()
        while(True):
            continue

#assist=music()
#assist.play('dynamite by bts')
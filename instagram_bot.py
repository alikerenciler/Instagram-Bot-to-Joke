from selenium import webdriver
from selenium.webdriver.common.keys import Keys
#from acount import password,gmail
import time

gmail = input("Enter gmail?: ")
password = input("Enter password?: ")
victim_id = input("Who is the victim?: ")

class Instagram():
    def __init__(self,gmail,password,victim_id):
        self.browserProfile = webdriver.ChromeOptions()
        self.browserProfile.add_experimental_option('prefs',{'intl.accept_languages':'en,en_US'})
        self.browser = webdriver.Chrome('chromedriver.exe',chrome_options=self.browserProfile)
        self.gmail = gmail
        self.password = password
        self.victim_id = victim_id

    def logIn(self): 
        #sign in to the acount
        
        self.browser.get("https://www.instagram.com/accounts/login/?next=/login/")
        time.sleep(2)

        gmail_input = self.browser.find_element_by_xpath("//*[@id='loginForm']/div/div[1]/div/label/input")
        password_input = self.browser.find_element_by_xpath("//*[@id='loginForm']/div/div[2]/div/label/input")
        gmail_input.send_keys(self.gmail)
        password_input.send_keys(self.password)
        time.sleep(1)
        password_input.send_keys(Keys.ENTER)
        time.sleep(3)

    def userInfo(self): 
        #goes to the your victim page and take her/his followers and following acount names
        
        self.browser.get(f"https://www.instagram.com/{self.victim_id}/")
        time.sleep(3)
        self.browser.find_element_by_xpath("//*[@id='react-root']/section/main/div/header/section/ul/li[2]/a").click()
        time.sleep(2)

        dialog = self.browser.find_element_by_css_selector("div[role=dialog] ul")

        followerCount = len(dialog.find_elements_by_css_selector("li"))
        

        action = webdriver.ActionChains(self.browser)
        while True:
            dialog.click()
            action.key_down(Keys.SPACE).key_up(Keys.SPACE).perform()
            action.key_down(Keys.SPACE).key_up(Keys.SPACE).perform()
            time.sleep(2)

            newCount = len(dialog.find_elements_by_css_selector("li"))
            
            if followerCount != newCount:
                followerCount = newCount
                print(f"Current followers number: {newCount}")
                time.sleep(1.5)
            else:
                break
        
        followers = dialog.find_elements_by_css_selector("li")
        followerList=[]
        for user in followers:
            link = user.find_element_by_css_selector("a").get_attribute("href")
            friends = link.replace("https://www.instagram.com/","")
            followerList.append(friends)
        
        print("*"*25+" Data has been saved "+"*"*25)
            
        self.browser.get(f"https://www.instagram.com/{self.victim_id}/")
        time.sleep(2)
        self.browser.find_element_by_xpath("//*[@id='react-root']/section/main/div/header/section/ul/li[3]/a/span").click()
        time.sleep(2)

        dialog2 = self.browser.find_element_by_css_selector("div[role=dialog] ul")

        followingCount = len(dialog2.find_elements_by_css_selector("li"))
        

        action2 = webdriver.ActionChains(self.browser)
        while True:
            dialog2.click()
            action2.key_down(Keys.SPACE).key_up(Keys.SPACE).perform()
            action2.key_down(Keys.SPACE).key_up(Keys.SPACE).perform()
            time.sleep(2)

            newCount2 = len(dialog2.find_elements_by_css_selector("li"))
            
            if followingCount != newCount2:
                followingCount = newCount2
                print(f"Current following number: {newCount2}")
                time.sleep(1.5)
            else:
                break

        following = dialog2.find_elements_by_css_selector("li")
        followingList=[]
        for user in following:
            link = user.find_element_by_css_selector("a").get_attribute("href")
            friends = link.replace("https://www.instagram.com/","")
            followingList.append(friends)
        
        # comes together in both lists and chooses which one is the same
        combination = []
        x = 0 
        for i in followerList:
            for d in followingList:
                if d == i :
                    combination.append(d)
                    x+=1
        print("*"*25+" Data has been saved "+"*"*25)

        # sends mesage to the victim 
        
        self.browser.get(f"https://www.instagram.com/{self.victim_id}/")
        time.sleep(3)
        self.browser.find_element_by_xpath("//*[@id='react-root']/section/main/div/header/section/div[1]/div[1]/div/div[1]/div/button").click()
        time.sleep(6)
        
        
        for i in combination:
            message = self.browser.find_element_by_xpath("//*[@id='react-root']/section/div/div[2]/div/div/div[2]/div[2]/div/div[2]/div/div/div[2]/textarea")
            message.send_keys(i)
            message.send_keys(Keys.ENTER)
            time.sleep(1)
        time.sleep(6)
        message2 = self.browser.find_element_by_xpath("//*[@id='react-root']/section/div/div[2]/div/div/div[2]/div[2]/div/div[2]/div/div/div[2]/textarea")
        explanation = "it was a joke :)"
        message2.send_keys(explanation)
        message2.send_keys(Keys.ENTER)
        print("all messages delivered!")


            
        

instagram = Instagram(gmail,password,victim_id)
instagram.logIn()
instagram.userInfo()

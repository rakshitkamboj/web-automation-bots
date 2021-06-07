from socket import SocketIO
from selenium import webdriver
from time import sleep




class InstaBot:
    def __init__(self,username,pw):
        x = username
        self.driver = webdriver.Chrome()
        self.driver.get("https://instagram.com")
        sleep(2)
        self.driver.find_element_by_xpath("//input[@name=\"username\"]").send_keys(username) 
        self.driver.find_element_by_xpath("//input[@name=\"password\"]").send_keys(pw)
        self.driver.find_element_by_xpath('//button[@type="submit"]').click()
        sleep(4)
        self.driver.find_element_by_class_name("s4Iyt").click()

        sleep(2)
        self.driver.find_element_by_xpath("//button[contains(text(), 'Not Now')]").click()
        sleep(2)
    def get_unfollowers(self):
        self.driver.find_element_by_xpath("//a[contains(@href,'/{}')]".format("rakshit.kamboj_")).click()
        sleep(2)
        self.driver.find_element_by_xpath("//a[contains(@href,'/following')]").click()
        
        following = self._get_name()

        self.driver.find_element_by_xpath("//a[contains(@href,'/followers')]").click()

        followers = self._get_name()

        not_following_back = [user for user in following if user not in followers]
        print(not_following_back)
    def _get_name(self):
        sleep(2)
        #self.driver.find_element_by_class_name("_8-yf5 ").click()
        scroll_box = self.driver.find_element_by_class_name("isgrP")
        
        
        last_ht, ht = 0,1
        while last_ht != ht:
            last_ht = ht
            sleep(1)
            ht = self.driver.execute_script("""
            arguments[0].scrollTo(0, arguments[0].scrollHeight);
            return arguments[0].scrollHeight;
            """,scroll_box)
        links = scroll_box.find_elements_by_tag_name("a")
        names = [name.text for name in links if name.text != ""]
        
        scroll_box.find_element_by_xpath("/html/body/div[5]/div/div/div[1]/div/div[2]/button").click()
        return names



my_bot = InstaBot("rakshit.kamboj_","*******")      
my_bot.get_unfollowers()
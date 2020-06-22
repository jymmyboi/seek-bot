from selenium import webdriver
from time import sleep

class seek_bot:
    def __init__(self, url):
        self.driver = webdriver.Chrome()
        self.driver.get(url)
        sleep(5)
        end = False
        while not(end): #cycling the pages
            jobs = self._get_names()
            for job in jobs:
                print(job) #formatting
            sleep(5)
            try: #clicking the 'next' button
                self.driver.find_element_by_class_name("bHpQ-bp").click()
                sleep(5)
            except:
                end = True

    def _get_names(self): #getting the names of the jobs
        links = self.driver.find_elements_by_class_name("_2iNL7wI")
        names = [name.text for name in links if name != '']
        return names
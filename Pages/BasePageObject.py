from selenium import webdriver
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By


class BasePageObject:
    """ 
        Base Page Object which handles general functions and driver. This class is to be inherited from other specific page objects.
    """
	
    EXP_WAIT_TIME = 20

    #class constructor. Instantiates driver if not included. Once driver is constructed, it is passed as reference between pages
    def __init__(self, driver=None):
        if driver: #if driver is included in the constructor, assign it to class
            self.driver = driver
        else: #if not, create new instance of webdriver
            self.driver = webdriver.Chrome()
        self.driver_wait = WebDriverWait(self.driver, self.EXP_WAIT_TIME) #set explicit wait time for web elements
		
    def get_element_by_class_name(self, class_name): #get a web element by its class name
        return self.driver_wait.until(ec.element_to_be_clickable((By.CLASS_NAME, class_name)))
		
    def get_element_by_href(self, href):#get a web element by its link
        return self.driver_wait.until(ec.element_to_be_clickable((By.XPATH, "//a[@href='"+ href + "']")))
	
    def get_element_by_text_name(self, text): #get a web element by its text
	    return self.driver_wait.until(ec.element_to_be_clickable((By.XPATH, "//*[contains(text(), '{0}')]".format(text))))

    def get_element_by_tag_name(self, tag_name): #get a web element by its tag name
        return self.driver_wait.until(ec.element_to_be_clickable((By.TAG_NAME, tag_name)))

    def get_element_by_attribute(self, attribute, value): #get a web element by its attribute
        return self.driver_wait.until(ec.element_to_be_clickable((By.XPATH, "//*[@{0}='{1}']".format(attribute, value))))

    def wait_for_loading_element_to_dissapear(self): # waits for the loading message to first appear, and then to dissapear to continue with duties.
        try:
            self.driver_wait.until(ec.visibility_of_element_located((By.CLASS_NAME, "loading-message")))
            return WebDriverWait(self.driver, 120).until(ec.invisibility_of_element_located((By.CLASS_NAME, "loading-message")))
        except:
            return None
		
    def stop(self): # closes webdriver.
        self.driver.quit()
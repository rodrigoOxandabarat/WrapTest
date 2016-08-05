from BasePageObject import BasePageObject
from PlanSelectionPage import PlanSelectionPage

class WrapInitialPage(BasePageObject):
    """ 
        Page Object that handles the Initial Page objects 
        and functions
    """
	#constructor. The initial page goes to url
    def __init__(self, driver=None):
        BasePageObject.__init__(self, driver)
        self.driver.get("https://www.qa.wrapdev.net/")
        self.driver.maximize_window()
		
    def login_link(self): # return the login link element
        return self.get_element_by_text_name("log in")
		
    def free_trial_link(self): #return the free trial link element
        return self.get_element_by_href("//authoring.qa.wrapdev.net/#/plans/select?scroll-to-pricing=true#introducingWrap")

    def click_on_free_trial_link(self):
        self.free_trial_link().click() #click on free trial link
        return PlanSelectionPage(self.driver)
